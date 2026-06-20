# Algorithms and Data Structures

## CS 320 Contact Service

**Language and tools:** Java and JUnit 5  
**Category:** Algorithms and Data Structures

### Artifact Overview

The original Contact Service used a single HashMap. It supported direct contact-ID lookup but did not support efficient last-name searching and used separate methods for each update operation.

### Completed Enhancements

- Retained a primary HashMap for direct contact-ID lookup.
- Added a TreeMap secondary index for ordered last-name and prefix searching.
- Added a unified `updateContact()` operation.
- Added `ContactNotFoundException` for missing-record failures.
- Trimmed String inputs before validation.
- Expanded JUnit coverage for shared last names, prefix matching, case handling, updates, and index consistency.

### Design Trade-Offs

The dual-index design uses additional memory and requires synchronization whenever a record changes. In exchange, it retains expected O(1) ID lookup and supports ordered TreeMap operations for last-name searching without a full O(n) scan.

### Artifact Files

- [Original ContactService.java](artifacts/cs320-contact-service/original/ContactService.java)
- [Enhanced ContactService.java](artifacts/cs320-contact-service/enhanced/ContactService.java)
- [Enhanced ContactNotFoundException.java](artifacts/cs320-contact-service/enhanced/ContactNotFoundException.java)
- [Web enhancement narrative](artifacts/cs320-contact-service/narrative)
- [Complete original, enhanced, test, and narrative package (ZIP)](CS499_Final_Portfolio_Artifacts.zip)

### Course Outcome Alignment

**Outcome 3:** The enhancement evaluates a performance limitation, selects a dual-index solution, and documents efficiency and maintenance trade-offs.

**Outcome 5:** Input trimming, validation, guard-then-act logic, and clearer exceptions improve data integrity and make invalid states easier to prevent and diagnose.
