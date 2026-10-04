# Generic Log Analysis Principles

This reference provides foundational knowledge for interpreting any structured or unstructured log format.

## Core Concepts
*   **Timestamps:** Always normalize timestamps to UTC in your reasoning to correlate events across multiple systems.
*   **Severity Levels:**
    *   `FATAL`/`CRITICAL`: Process crash.
    *   `ERROR`: Operation failed, but process may continue.
    *   `WARN`: Degraded state, retries occurring, or nearing thresholds.
    *   `INFO`: Normal lifecycle events (startup, shutdown, batch complete).
*   **Correlation IDs:** (Trace IDs, Request IDs). Use these strings to tie together logs from a frontend gateway all the way down to a database query.

## Distinguishing Errors vs. Noise
*   A single `WARN` followed by `INFO` usually indicates a successful retry. This is noise.
*   A cascading chain of `ERROR` logs across multiple components often points to a single root cause at the bottom of the stack (e.g., Database offline causes API to fail, causing Frontend to fail). Always hunt for the *first* error in the timeline.
