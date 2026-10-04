# Databricks Delta Live Tables (DLT) Pipeline Analysis

## Semantics
*   **Event Logs:** DLT surfaces operational data via the Event Log. Look for events with `level = 'ERROR'`.
*   **Expectations:** DLT uses "Expectations" for data quality. Look for `flow_progress.data_quality.dropped_records`. High drop counts indicate upstream data issues, not necessarily pipeline crashes.

## Common Patterns
*   `Flow Initialization Failure`: Indicates a schema resolution issue or invalid SQL/Python syntax in the pipeline definition.
*   `ConcurrentAppendException`: Multiple writers are trying to modify the same Delta table simultaneously without isolation guarantees.
