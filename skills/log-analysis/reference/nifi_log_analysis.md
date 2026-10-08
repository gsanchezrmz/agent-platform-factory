# NiFi Log Analysis

## Semantics
*   **Bulletin Board:** NiFi emits WARN/ERROR bulletins at the processor level. Look for the specific `Processor Name` and `Processor ID`.
*   **Yielding:** If a log mentions a processor is "yielding", it encountered a transient error (like a network blip) and is pausing execution to avoid spamming errors.
*   **Penalization:** FlowFiles are "penalized" when routed to a failure relationship, delaying their retry.

## Common Patterns
*   `OutOfMemoryError`: Usually indicates a processor tried to load a massive FlowFile entirely into JVM heap memory (e.g., using `ReplaceText` on a 5GB file) rather than streaming it.
*   `SocketTimeoutException`: Common in HTTP or Database processors. Indicates the downstream system is slow or unresponsive.
