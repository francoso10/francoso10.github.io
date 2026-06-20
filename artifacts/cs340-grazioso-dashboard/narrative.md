# CS 340 Grazioso Salvare Dashboard - Enhancement Narrative

## Artifact Description

The selected artifact is the Grazioso Salvare Dashboard from CS 340: Client/Server Development. The project connects a Python and JupyterDash interface to MongoDB through an AnimalShelter CRUD module. It filters rescue-category animals, displays records in a Dash DataTable, visualizes breed distribution with Plotly, and maps selected animals by location.

The original application was functional, but it relied on hardcoded connection values, had limited query protection, did not model role-based access boundaries, and did not include an indexing strategy for repeated rescue-filter queries.

## Enhancement Description

The enhanced CRUD module reads database configuration from environment variables or constructor arguments and includes a safe `.env.example` template. It applies recursive NoSQL query sanitization with an allowlist of approved MongoDB operators. It also introduces application-level roles: the dashboard uses read-only access, while create, update, delete, and index operations require elevated editor or administrator roles.

The enhancement adds indexes for frequently used rescue-filter fields, including breed, animal type, sex upon outcome, age upon outcome in weeks, and the primary compound query pattern. The dashboard was updated to use the read-only role and to handle connection errors, empty results, logo-file differences, and map data through named columns instead of fixed positions.

## Course Outcome Alignment

This enhancement supports Outcome 1 by modeling appropriate access boundaries for organizational decision-making. It supports Outcome 3 through index selection and performance trade-offs. It supports Outcome 4 through secure configuration, authorization, validation, and indexing techniques. It strongly supports Outcome 5 through credential protection, query validation, least privilege, and safer database operations.

## Reflection

The work changed how I evaluate applications. Rather than considering only whether a dashboard works, I considered who can access it, which queries should be accepted, which operations require elevated privileges, and how the database should support repeated use efficiently. The final artifact is more secure, maintainable, and aligned with governance and risk considerations.
