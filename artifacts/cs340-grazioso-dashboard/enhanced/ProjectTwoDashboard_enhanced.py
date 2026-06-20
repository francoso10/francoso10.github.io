"""Enhanced Dash dashboard for the CS 340 Grazioso Salvare artifact."""

from jupyter_dash import JupyterDash
import base64
import os

import dash_leaflet as dl
import pandas as pd
import plotly.express as px
from dash import dash_table, dcc, html
from dash.dependencies import Input, Output

from animal_shelter import AnimalShelter

JupyterDash.infer_jupyter_proxy_config()

DASHBOARD_COLUMNS = [
    "animal_id", "name", "animal_type", "breed", "sex_upon_outcome",
    "age_upon_outcome_in_weeks", "location_lat", "location_long",
]

try:
    db = AnimalShelter(role="read")
    connection_error = None
except Exception as exc:
    db = None
    connection_error = str(exc)


def load_data(query=None):
    if db is None:
        return pd.DataFrame(columns=DASHBOARD_COLUMNS)
    dff = pd.DataFrame.from_records(db.read(query or {}))
    if "_id" in dff.columns:
        dff.drop(columns=["_id"], inplace=True)
    return dff


def build_query(filter_type):
    if filter_type == "water":
        return {"$and": [
            {"animal_type": "Dog"},
            {"breed": {"$in": ["Labrador Retriever Mix", "Chesapeake Bay Retriever", "Newfoundland"]}},
            {"sex_upon_outcome": "Intact Female"},
            {"age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}},
        ]}
    if filter_type == "mountain":
        return {"$and": [
            {"animal_type": "Dog"},
            {"breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog", "Siberian Husky", "Rottweiler"]}},
            {"sex_upon_outcome": "Intact Male"},
            {"age_upon_outcome_in_weeks": {"$gte": 26, "$lte": 156}},
        ]}
    if filter_type == "disaster":
        return {"$and": [
            {"animal_type": "Dog"},
            {"breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever", "Bloodhound", "Rottweiler"]}},
            {"sex_upon_outcome": "Intact Male"},
            {"age_upon_outcome_in_weeks": {"$gte": 20, "$lte": 300}},
        ]}
    return {}


df = load_data({})
app = JupyterDash(__name__)

logo_path = next((p for p in ["Grazioso Salvare Logo (1).png", "Grazioso Salvare Logo.png"] if os.path.exists(p)), None)
encoded_logo = ""
if logo_path:
    with open(logo_path, "rb") as image_file:
        encoded_logo = base64.b64encode(image_file.read()).decode()

status_message = "Connected using read-only dashboard role."
if connection_error:
    status_message = f"Database connection not available: {connection_error}"

app.layout = html.Div([
    html.Center(html.Img(src=f"data:image/png;base64,{encoded_logo}", style={"height": "120px"}) if encoded_logo else html.Div()),
    html.Center(html.B(html.H1("CS-340 Dashboard - Francisco Sousa"))),
    html.Center(html.P(status_message)),
    dcc.RadioItems(
        id="filter-type",
        options=[
            {"label": "Water Rescue", "value": "water"},
            {"label": "Mountain/Wilderness", "value": "mountain"},
            {"label": "Disaster/Tracking", "value": "disaster"},
            {"label": "Reset", "value": "reset"},
        ],
        value="reset",
        labelStyle={"display": "inline-block", "margin-right": "18px"},
    ),
    dash_table.DataTable(
        id="datatable-id",
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict("records"),
        page_size=12,
        filter_action="native",
        sort_action="native",
        row_selectable="single",
        selected_rows=[0] if not df.empty else [],
    ),
    html.Div(style={"display": "flex"}, children=[html.Div(id="graph-id"), html.Div(id="map-id")]),
])


@app.callback(Output("datatable-id", "data"), [Input("filter-type", "value")])
def update_dashboard(filter_type):
    return load_data(build_query(filter_type)).to_dict("records")


@app.callback(Output("graph-id", "children"), [Input("datatable-id", "derived_virtual_data")])
def update_graphs(view_data):
    dff = pd.DataFrame(view_data) if view_data else pd.DataFrame()
    if dff.empty or "breed" not in dff.columns:
        return [html.P("No breed data available for the selected filter.")]
    counts = dff["breed"].value_counts().reset_index()
    counts.columns = ["breed", "count"]
    return [dcc.Graph(figure=px.pie(counts, names="breed", values="count", title="Breed Distribution in Current Filter"))]


@app.callback(Output("map-id", "children"), [Input("datatable-id", "derived_virtual_data"), Input("datatable-id", "derived_virtual_selected_rows")])
def update_map(view_data, selected_rows):
    if not view_data:
        return [html.P("No location data available.")]
    dff = pd.DataFrame.from_dict(view_data)
    if dff.empty or "location_lat" not in dff.columns or "location_long" not in dff.columns:
        return [html.P("Location columns are unavailable.")]
    row = selected_rows[0] if selected_rows else 0
    if row >= len(dff):
        row = 0
    lat = dff.iloc[row].get("location_lat")
    lon = dff.iloc[row].get("location_long")
    if pd.isna(lat) or pd.isna(lon):
        return [html.P("Selected animal does not have valid coordinates.")]
    return [dl.Map(style={"width": "1000px", "height": "500px"}, center=[30.75, -97.48], zoom=10, children=[dl.TileLayer(), dl.Marker(position=[lat, lon])])]


app.run_server()
