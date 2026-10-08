---
scope: "global"
agents:
  - replication-monitoring-agent
  - data-quality-agent
---

# Rule: Strict Separation of Fact and Inference

This rule applies universally to all investigation agents on the Data Platform.

## Core Principle
You must NEVER present a deduction, assumption, or generated explanation as a fact.

## Execution Standard
When outputting reports, logs, or user messages, use explicit prefixes:

*   **[FACT]**: Information directly returned by a deterministic Tool or MCP server.
    *   *Correct:* `[FACT] Hangfire job 1234 returned status FAILED.`
    *   *Incorrect:* `[FACT] Hangfire failed because of a network timeout.` (Unless the error explicitly said "network timeout").
*   **[INFERENCE]**: Your reasoning based on the facts and your skills.
    *   *Correct:* `[INFERENCE] Because Kafka lag is 5000 and Databricks is FAILED, I infer the consumer is dead.`
*   **[UNKNOWN]**: When a tool fails to return data, or a system is unreachable.

Violation of this standard is considered a critical hallucination risk and will cause the evaluation suite to fail the run.
