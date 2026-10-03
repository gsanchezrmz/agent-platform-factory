# ADR 0001: Initial Architecture and Platform/Domain Separation

## Status
Accepted

## Context
We need to build a Data Platform Agent Engineering Platform capable of supporting multiple agents (e.g., Replication Monitoring, Data Quality) while maintaining strict security, policy enforcement, and domain separation.

## Decision
We will enforce a strict separation between the **Platform Core** and the **Data Platform Domain**.

- **Platform Core:** Contains the Agent Contract, Workflow definitions, Tool abstractions (MCP), Policy Engine, Observability, and Evaluation framework. It knows nothing about data replication or Databricks.
- **Domain/Integrations:** Contains specific entities (Databases, Replication Configurations) and MCP servers (or mocks for the MVP) that interface with specific systems (Kafka, NiFi).
- **Agents:** Are instances defined by a Contract that wire together Platform capabilities with Domain tools.

## Consequences
- **Positive:** We can build a Data Quality Agent using the exact same Platform Core without modifying it.
- **Negative:** Initial overhead of building abstract interfaces (like the Policy Engine and MCP wrappers) before implementing the actual agent logic.

## Compliance with Requirements
This directly addresses the requirement to build an "Agent Engineering Platform" first, rather than just building a "Replication Monitoring Agent".