# Databases

## CS 340 Grazioso Salvare Dashboard

**Language and tools:** Python, JupyterDash, Dash, Plotly, MongoDB, and PyMongo  
**Category:** Databases

### Artifact Overview

This artifact is a browser-based animal shelter dashboard created for CS 340: Client/Server Development. The original application connected a Dash interface to MongoDB through a custom CRUD module, filtered rescue-category animals, displayed results in a DataTable, visualized breed distribution, and mapped a selected animal.

The original application used hardcoded connection settings, had limited query protection, did not define role-based access boundaries, and did not include an indexing strategy for repeated rescue-filter queries.

### Completed Enhancements

- Replaced hardcoded connection settings with environment-based configuration.
- Added `.env.example` without live credentials.
- Added recursive NoSQL query sanitization with an allowlist of approved operators.
- Added application-level read-only, editor, and administrator roles.
- Added indexes for rescue-filter fields and the main compound query pattern.
- Updated dashboard behavior for read-only access, errors, empty results, logo references, and map columns.

### Artifact Files

- [Original CRUD module - public-safe redacted copy](artifacts/cs340-grazioso-dashboard/original/animal_shelter.py)
- [Enhanced CRUD module](artifacts/cs340-grazioso-dashboard/enhanced/animal_shelter.py)
- [Enhanced dashboard source](artifacts/cs340-grazioso-dashboard/enhanced/ProjectTwoDashboard_enhanced.py)
- [Safe environment template](artifacts/cs340-grazioso-dashboard/enhanced/.env.example)
- [Web enhancement narrative](artifacts/cs340-grazioso-dashboard/narrative)

### Security and Governance Considerations

The dashboard uses read-only access while higher-risk operations require elevated permissions. The query sanitizer limits accepted operators to the subset required by the application. Sensitive configuration values are excluded from the public portfolio.

### Course Outcome Alignment

**Outcome 1:** The dashboard supports organizational decision-making and models appropriate access levels for different users.

**Outcome 3:** Indexing decisions improve repeated query performance while requiring consideration of index-maintenance overhead.

**Outcome 4:** The enhancement applies practical configuration, authorization, validation, and indexing techniques to a full-stack application.

**Outcome 5:** Environment-based configuration, query sanitization, least privilege, and safer database operations strengthen security.
