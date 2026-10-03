# FastMCP Strategy

## Purpose
This document outlines our strategy for adopting Model Context Protocol (MCP) using the FastMCP framework for building tools and integrations for the Data Platform Agent.

## Scope of FastMCP
FastMCP will be used as the primary interface standard for creating custom tools that the agents can interact with.

### Included in MVP
- **Tools:** We will define tools (e.g., `check_replication_status`, `query_bronze_layer`) using FastMCP's tool abstractions. This allows agents to execute specific actions.
- **Structured Outputs:** FastMCP schemas will be used to ensure tools return predictable, structured JSON outputs to the LLM.
- **Error Handling:** FastMCP's built-in error handling will be leveraged to provide clear, actionable feedback to the agent when an operation fails.

### Deferred / Excluded from MVP
- **Resources:** For the MVP, we will primarily use Tools to dynamically fetch data rather than pre-defining static Resources.
- **Prompts (Server-side):** We will manage agent prompts within the Agent Engineering Platform rather than relying on MCP server-side prompts.
- **Complex Authentication:** The MVP uses mock integrations. Real authentication (OAuth, mTLS) to backing systems is deferred, but the platform's Policy Engine will simulate authorization checks before routing to FastMCP.

## Security Implications
- FastMCP servers must be treated as untrusted boundaries.
- The Agent Engine will enforce policy *before* sending a request to the FastMCP server.
- The FastMCP server must validate all inputs against its schema to prevent injection attacks.

## Implementation Details
We will wrap our specific domain logic (e.g., Databricks, Kafka, Hangfire mocks) in FastMCP server instances, which the `MCP Abstraction` layer of our core platform will communicate with.