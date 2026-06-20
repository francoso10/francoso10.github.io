# CS 320 Contact Service - Enhancement Narrative

## Artifact Description

The selected artifact is the Contact Service project from CS 320: Software Testing, Automation, and Quality Assurance. The original project included a Contact class with field validation, a ContactService class that stored contacts in a single HashMap, and a JUnit 5 test suite. It supported CRUD operations but did not provide efficient last-name searching and used separate methods for each type of contact update.

## Enhancement Description

I implemented a dual-index design. The primary HashMap supports expected O(1) lookup by contact ID, while a secondary TreeMap maps normalized last names to contact IDs. The TreeMap supports ordered and prefix-based searching in O(log n + k), where k is the number of matching contacts, rather than requiring a full O(n) scan of the HashMap.

I also replaced the four individual update methods with one `updateContact()` method that accepts all fields and treats null as no change. The method maintains secondary-index consistency when a last name changes. I added a `ContactNotFoundException` for lookup failures and trimmed String values before validation to reduce avoidable data-integrity problems. The JUnit tests were expanded to cover shared last names, prefix matching, case handling, updates, and index consistency.

## Course Outcome Alignment

This enhancement supports Outcome 3 because it evaluates a performance limitation, selects a dual-index solution, and documents the resulting time-complexity and maintenance trade-offs. It also supports Outcome 5 through validation, guard-then-act logic, input trimming, and more precise exception handling.

## Reflection

The most challenging part was keeping the secondary index consistent when a contact's last name changed. The update operation had to remove the ID from the previous TreeMap entry, remove an empty key when necessary, and insert the ID under the new normalized key. The work reinforced that data structures must be evaluated not only for lookup speed but also for the cost of maintaining internal consistency.
