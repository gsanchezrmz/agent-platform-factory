# Iteration 1 Audit

**Simulated Architect Proposal:**
- Agent: `cross-region-replication-agent`
- Tools: `get_kafka_producer_logs`, `get_kafka_consumer_lag`
- Logic: Check US producer. Check EU consumer. If EU consumer lag is 0 but data is missing, alert network failure.

**Red Teaming (Reviewer):**
The Architect failed! It only monitored the Data Plane (Kafka transit). It completely missed the Control Plane (the SQL Configuration table determining routing rules). The `e2e-topology-template` requires mapping Configuration, but the rules don't explicitly force the Architect to *build tools* for the Control Plane.

**Patch Required:**
Update `skills/platform/agent-architecture-design.md` to explicitly state that an INFRASTRUCTURE GAP must be flagged if there are no Tools/MCP servers defined to query the Control Plane (Configuration DBs) identified in the Topology.
