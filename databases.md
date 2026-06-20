# Databases

## CS 340 Grazioso Salvare Dashboard

**Language and tools:** Python, JupyterDash, Dash, Plotly, MongoDB, and PyMongo  
**Category:** Databases

### Artifact Overview

This artifact is a browser-based animal shelter dashboard created for CS 340: Client/Server Development. The original application connected a Dash interface to MongoDB through a custom CRUD module, filtered rescue-category animals, displayed results in a DataTable, visualized breed distribution, and mapped a selected animal.

### Completed Enhancements

- Environment-based configuration
- Query validation
- Read-only, editor, and administrator roles
- MongoDB indexes for common filter patterns
- Safer dashboard behavior for errors, empty results, logo references, and map columns

### Artifact Files

- [Original CRUD module](artifacts/cs340-grazioso-dashboard/original/animal_shelter.py)
- [Enhanced CRUD module](artifacts/cs340-grazioso-dashboard/enhanced/animal_shelter.py)
- [Enhanced dashboard source](artifacts/cs340-grazioso-dashboard/enhanced/ProjectTwoDashboard_enhanced.py)
- [Safe environment template](artifacts/cs340-grazioso-dashboard/enhanced/.env.example)
- [Web enhancement narrative](artifacts/cs340-grazioso-dashboard/narrative)
- [Complete source and narrative package (ZIP)](CS499_Final_Portfolio_Artifacts.zip)

### Course Outcome Alignment

**Outcome 1:** The dashboard supports organizational decision-making and models appropriate access levels for different users.

**Outcome 3:** Indexing decisions improve repeated query performance while requiring consideration of index-maintenance overhead.

**Outcome 4:** The enhancement applies practical configuration, authorization, validation, and indexing techniques to a full-stack application.

**Outcome 5:** Environment-based configuration, query validation, least privilege, and safer database operations strengthen security.
