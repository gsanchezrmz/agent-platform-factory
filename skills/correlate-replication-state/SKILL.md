# Skill: Correlate Replication State

This skill instructs the agent on how to synthesize the Evidence Matrix into a single Root Cause.

## Purpose
To provide the user with a definitive answer to "Why is replication broken?" rather than a raw dump of metrics.

## Procedural Knowledge

Apply the following correlation matrix to the evidence gathered:

1.  If `hangfire_state == FAILED`:
    *   **Root Cause:** Source Extraction Failure.
    *   **Explanation:** Data is not leaving the source system. Downstream systems are healthy but starved of data.
2.  If `hangfire_state == SUCCESS` AND `nifi_state == BACKED_UP`:
    *   **Root Cause:** Ingestion Bottleneck.
    *   **Explanation:** Source is pushing data, but NiFi is failing to process and route it to Kafka.
3.  If `kafka_state == LAGGING` AND `databricks_state == FAILED`:
    *   **Root Cause:** Target Processing Failure.
    *   **Explanation:** Data has successfully transported to Kafka, but the Databricks consumer is failing to process the messages into the Bronze layer.

## Failure Handling
* If the state combination does not match the above rules, state: "INFERENCE: Complex or unknown failure. Manual engineering review required."
