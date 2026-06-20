---
layout: default
title: Algorithms and Data Structures
---

# Algorithms and Data Structures

## CS 320 Contact Service

**Language and tools:** Java and JUnit 5  
**Category:** Algorithms and Data Structures

### Artifact Overview

This artifact is the Contact Service project created for CS 320: Software Testing, Automation, and Quality Assurance. The original project provided contact creation, update, deletion, validation, and unit testing. Contacts were stored in a single HashMap, which supported efficient lookup by contact ID but did not support efficient searching by last name.

### Enhancement Goal

The enhancement focused on improving search capability while preserving fast contact-ID access. The design adds a secondary index and strengthens the consistency, validation, and testing of the service.

### Completed Enhancements

- Kept a primary HashMap for direct contact-ID lookup.
- Added a secondary TreeMap that maps normalized last names to contact IDs.
- Added efficient ordered and prefix-based last-name searching.
- Consolidated separate field-update methods into a single `updateContact()` method.
- Added a `ContactNotFoundException` for clearer handling of missing records.
- Trimmed String values before validation to prevent avoidable data-integrity problems.
- Expanded JUnit 5 tests for shared last names, case handling, prefix boundaries, updates, and index consistency.

### Design Trade-Offs

The dual-index design uses additional memory and requires careful synchronization when a contact is added, updated, or deleted. In exchange, it retains expected O(1) direct lookup by contact ID and supports ordered TreeMap operations for last-name searching, rather than requiring a full O(n) scan through every contact.

### Skills Demonstrated

- Data-structure selection based on performance needs
- Big-O reasoning and trade-off analysis
- Consistency management across multiple indexes
- Defensive input validation
- Exception design
- Unit and edge-case testing

### Course Outcome Alignment

**Outcome 3: Algorithmic principles and computing practices.** The enhancement evaluates a performance limitation, selects a dual-index solution, and documents the efficiency and maintenance trade-offs.

**Outcome 5: Security mindset.** Input trimming, validation, guard-then-act logic, and clearer exceptions improve data integrity and make invalid states easier to prevent and diagnose.

### Portfolio Materials

The final portfolio package will include the original source, enhanced source, JUnit tests, and enhancement narrative for this artifact.

[Back to portfolio home](./)
