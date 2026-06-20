---
layout: default
title: Databases
---

# Databases

## CS 340 Grazioso Salvare Dashboard

**Language and tools:** Python, JupyterDash, Dash, Plotly, MongoDB, and PyMongo  
**Category:** Databases

### Artifact Overview

This artifact is a browser-based animal shelter dashboard created for CS 340: Client/Server Development. The original application connects to a MongoDB database through a custom CRUD module, filters animals by rescue category, displays results in a Dash DataTable, visualizes breed distribution with a Plotly chart, and maps a selected animal using geographic coordinates.

The original application demonstrated functional database access and visualization, but it relied on hardcoded connection settings, had limited query protection, did not define role-based access boundaries, and did not include an indexing strategy for repeated rescue-filter queries.

### Enhancement Goal

The enhancement focused on improving the dashboard as a secure, maintainable, and auditable data-driven application. The work addresses how credentials are handled, which database queries are accepted, who can perform higher-risk actions, and how the database supports repeated filtering efficiently.

### Completed Enhancements

- Replaced hardcoded database configuration with environment-based settings and safe constructor configuration.
- Added a `.env.example` template that documents required settings without exposing sensitive values.
- Added recursive NoSQL query sanitization using an allowlist of approved MongoDB operators.
- Added application-level role-based access control for read-only, editor, and administrative operations.
- Added indexes for frequently queried rescue-filter fields, including breed, animal type, sex upon outcome, age upon outcome in weeks, and the primary compound query pattern.
- Updated the dashboard to use a read-only connection and improved handling for errors, empty results, the logo reference, and map callback columns.

### Security and Governance Considerations

This enhancement applies least privilege by ensuring the dashboard uses read-only access while higher-risk operations require elevated permissions. The query sanitizer limits accepted operators to the subset required by the application, reducing exposure to unexpected or high-risk query behavior. The public portfolio version will not include active credentials, environment files, connection strings, or other sensitive configuration values.

### Skills Demonstrated

- Secure database configuration
- NoSQL query validation and sanitization
- Role-based access control and least privilege
- MongoDB indexing and query-performance trade-offs
- Dashboard integration with a secured CRUD layer
- Risk-aware and auditable system design

### Course Outcome Alignment

**Outcome 1: Collaborative environments and organizational decision-making.** The dashboard supports data-driven decisions, while its role model demonstrates how users can receive appropriate access based on responsibility.

**Outcome 3: Algorithmic principles and computing practices.** Indexing decisions improve repeated query performance while requiring consideration of index-maintenance overhead.

**Outcome 4: Innovative techniques, skills, and tools.** The enhancement applies practical configuration, authorization, validation, and indexing techniques to strengthen a functional full-stack application.

**Outcome 5: Security mindset.** Environment-based configuration, query sanitization, least privilege, and safer error handling strengthen the confidentiality, integrity, and reliability of database operations.

### Portfolio Materials

The final portfolio package will include a public-safe original artifact, enhanced source, `.env.example`, tests, project documentation, and the enhancement narrative. Sensitive configuration values are excluded.

[Back to portfolio home](./)
