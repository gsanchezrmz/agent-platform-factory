# Skill: Investigate NiFi Failures

This skill provides domain knowledge on how to interpret NiFi processor backlogs and errors within the context of Data Platform replication.

## Purpose
To correctly identify if a NiFi processor is bottlenecked due to configuration, thread starvation, or downstream backpressure.

## When to use
* You have gathered evidence showing `QueuedFlowFiles > 1000` or `nifi_state == BACKED_UP`.

## Procedural Knowledge

1.  **Analyze Active Threads:**
    *   If `ActiveThreads == 0` and `QueuedFlowFiles > 0`: The processor is likely stopped or errored out.
    *   If `ActiveThreads > 0` and `QueuedFlowFiles` is steadily increasing: The processor is working but is bottlenecked (likely due to downstream backpressure).

## Expected Output
When analyzing NiFi, output a structured statement:
*   **FACT:** NiFi Processor X has Y queued flowfiles and Z active threads.
*   **INFERENCE:** The processor is [STOPPED | BOTTLENECKED].
