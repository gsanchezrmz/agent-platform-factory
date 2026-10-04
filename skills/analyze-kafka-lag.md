# Skill: Analyze Kafka Lag

This skill provides domain knowledge on how to interpret Kafka lag within the context of Data Platform replication.

## Purpose
To correctly differentiate between transient processing spikes and systemic failures based on Kafka consumer lag metrics.

## When to use
* You have gathered evidence showing `CurrentLag > 0`.
* You need to determine if the lag is acceptable or indicative of a broken Databricks ingest.

## Procedural Knowledge

1.  **Understand the Thresholds:**
    *   `Lag == 0`: Perfectly healthy.
    *   `0 < Lag < 1000`: Normal micro-batching variance. *Inference: Transient spike.*
    *   `Lag >= 1000` AND `LagRate > 0`: Systemic backlog. Consumer is failing to keep up or is dead. *Inference: Ingestion failure.*

2.  **Correlate with Databricks:**
    *   If Kafka is lagging heavily (>= 1000), you MUST check Databricks.
    *   If Databricks `JobState` is `IDLE` or `FAILED`, the root cause is the Databricks cluster, not Kafka itself.

## Expected Output
When analyzing lag, output a structured statement:
*   **FACT:** Kafka Topic X has Y lag.
*   **INFERENCE:** The lag is [TRANSIENT | SYSTEMIC].
*   **RECOMMENDATION:** [Wait 5 minutes | Investigate downstream Databricks job].
