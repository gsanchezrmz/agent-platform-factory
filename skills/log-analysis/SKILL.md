---
name: log-analysis
description: "Universal procedure for extracting, structuring, and analyzing diagnostic evidence from application and infrastructure logs."
when_to_use: "When interpreting raw text logs, stack traces, or diagnostic payloads retrieved from tools or MCP servers."
dependencies:
  - "skills/log-analysis/reference/generic_log_analysis.md"
  - "skills/log-analysis/reference/csharp_log_analysis.md"
  - "skills/log-analysis/reference/sql_error_analysis.md"
  - "skills/log-analysis/reference/nifi_log_analysis.md"
  - "skills/log-analysis/reference/kafka_log_analysis.md"
  - "skills/log-analysis/reference/databricks_log_analysis.md"
  - "skills/log-analysis/reference/databricks_pipeline_analysis.md"
---

# Log Analysis Procedure

## Overview
This Skill defines the universal cognitive process an AI Agent must use when reading log data. It ensures investigations are rigorous, evidence-based, and free of hallucination.

## Procedure

### 1. Evidence Extraction
*   Identify the source technology of the log payload.
*   Load the appropriate `reference/` material (e.g., if it's a Databricks log, consult `databricks_log_analysis.md`).
*   Extract the core components of the log: Timestamp, Severity (ERROR, WARN, INFO), Correlation IDs, and the exact Error Message / Stack Trace.

### 2. Error Classification
*   Determine if the error is:
    *   **Infrastructure:** Network timeout, disk full, memory limit.
    *   **Application/Logic:** Null reference, syntax error, division by zero.
    *   **Authentication/Authorization:** Expired token, missing permissions.
    *   **Dependency:** Downstream API is returning 500s.

### 3. Behavioral Analysis (Retries & Timeouts)
*   Look for patterns. Is this a single isolated error, or a repeating timeout loop?
*   Identify if the system is attempting retries. A repeating warning followed by a final error indicates exhaustion of a retry policy.

### 4. Distinguish FACT from INFERENCE
You must explicitly categorize your findings in your output.
*   **[FACT]:** What the log explicitly states. (e.g., "The log contains `TimeoutException` at 10:04 UTC").
*   **[INFERENCE]:** What you deduce using the reference material. (e.g., "Because a `TimeoutException` occurred repeatedly over 5 minutes, I infer the downstream API is unreachable").

### 5. Identify Missing Evidence
*   If the log does not contain enough information to determine the root cause, do NOT guess.
*   State: "Insufficient evidence."
*   Identify what additional telemetry or logs are required (e.g., "Need the Kafka broker logs to confirm why the consumer was disconnected").
