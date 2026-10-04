# SQL Error Analysis

## Semantics
*   **Syntax Errors:** Usually caught during deployment/testing, but if seen in production, indicates dynamic SQL gone wrong.
*   **Deadlocks:** (e.g., SQL Server Error 1205). Occurs when two concurrent transactions block each other. The victim transaction is rolled back.
*   **Timeout Expired:** Indicates the query took longer than the configured `CommandTimeout`. Usually caused by missing indexes, parameter sniffing, or blocking locks.

## Common Patterns
*   `Violation of PRIMARY KEY constraint`: Attempting to insert a duplicate record.
*   `String or binary data would be truncated`: Attempting to insert text that is larger than the column's defined `VARCHAR` length.
