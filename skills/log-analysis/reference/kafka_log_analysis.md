# Kafka Log Analysis

## Semantics (Broker vs Client)
*   Ensure you identify if the log is from a Broker (infrastructure) or a Producer/Consumer (application).
*   **Offsets:** References to `CommitFailedException` indicate a consumer took too long to process a batch and the broker gave its partition to another consumer.

## Common Patterns
*   `RebalanceInProgress`: Consumers are joining/leaving the group. Processing pauses during this time. Continual rebalancing indicates unstable consumers.
*   `RecordTooLargeException`: A producer attempted to send a message exceeding the broker's `message.max.bytes` configuration.
*   `NotLeaderOrFollowerException`: A transient error occurring during broker failover. Clients should automatically retry.
