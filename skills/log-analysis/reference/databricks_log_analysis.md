# Databricks Cluster & Job Log Analysis

## Semantics
*   **Driver vs. Worker:** Distinguish between Driver logs (coordinating the Spark job) and Worker logs (executing the tasks).
*   **OOM (Out of Memory):**
    *   *Driver OOM:* Usually caused by `collect()` bringing too much data to the master node.
    *   *Executor OOM:* Caused by highly skewed partitions or data explosion during joins.

## Common Patterns
*   `SparkException: Job aborted due to stage failure`: This is a generic wrapper. You MUST read further down the stack trace to find the `Caused by:` clause, which contains the actual error (e.g., a data type mismatch or S3 access denied).
*   `Cluster Startup Failures`: Often related to cloud quotas, invalid init scripts, or missing library dependencies.
