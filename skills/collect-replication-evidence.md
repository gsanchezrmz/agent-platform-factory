# Skill: Collect Replication Evidence

This skill defines the standard procedure for gathering telemetry across the replication stack when an incident is reported.

## Purpose
To ensure a comprehensive and deterministic gathering of facts before any root cause analysis begins.

## When to use
* A user reports a replication delay.
* An automated alert fires regarding a pipeline failure.
* The `replication-investigation-workflow` instructs you to gather state.

## Required Context
* `pipeline_id` or `table_name`
* `environment` (e.g., dev, prod)
* `approximate_incident_time`

## Investigation Procedure

When invoked, you MUST execute these steps in order, using the provided tools:

1.  **Check Source (Hangfire):**
    *   Call `get_hangfire_job_status` with the `pipeline_id`.
    *   *Evidence requirement:* Note the `LastExecutionTime`, `Status`, and any `ExceptionDetails`.
2.  **Check Transport (NiFi & Kafka):**
    *   If Hangfire succeeded, call `get_nifi_processor_status` for the associated ingest processor.
    *   Call `get_kafka_lag` for the destination topic.
    *   *Evidence requirement:* Note `QueuedFlowFiles` in NiFi and `CurrentLag` in Kafka.
3.  **Check Processing (Databricks):**
    *   If transport is healthy (no lag, no queued files), call `get_databricks_pipeline_state` for the Raw-to-Bronze job.
    *   *Evidence requirement:* Note the `JobState` and `LastProcessedTimestamp`.

## Output Formulation
You must produce an "Evidence Matrix" structured exactly like this:
```json
{
  "hangfire_state": "SUCCESS | FAILED | UNKNOWN",
  "nifi_state": "HEALTHY | BACKED_UP | UNKNOWN",
  "kafka_state": "CAUGHT_UP | LAGGING | UNKNOWN",
  "databricks_state": "PROCESSING | FAILED | IDLE"
}
```

## Constraints
* Do not attempt to fix any failures discovered during this phase.
* If a tool returns an error, record the state as `UNKNOWN` and log the error message as FACT.
