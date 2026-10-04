# FastMCP Strategy

This document outlines the strategy for integrating Model Context Protocol (MCP) and FastMCP into the Data Platform Agent Engineering Platform.

## 1. Why MCP is used in this platform
MCP provides a standardized, interoperable protocol for agents to access external systems, read context, and execute tools. It allows decoupling the platform runtime from the specifics of every enterprise domain system.

## 2. What capabilities should be exposed through MCP
* Read-only telemetry and log extraction (e.g., NiFi status, Kafka lag).
* Domain-specific toolkits that exist outside the core platform repository.
* Corporate enterprise systems (Jira, GitHub) where existing MCP servers already exist.

## 3. When to use MCP versus a direct deterministic adapter/tool
* **Use MCP when:** Integrating with external enterprise systems, building distinct microservice capabilities, or consuming third-party tools.
* **Use Direct Adapters when:** The tool is intrinsic to the platform's orchestration, tightly coupled to core performance, or when deploying a separate MCP server is operationally unjustified for a simple Python function.

## 4. Platform Role: Client or Server?
The Data Platform Agent Engineering Platform acts primarily as an **MCP Client**. It dynamically loads approved MCP servers defined in the Agent Engineering Artifacts and connects to them to provide tools to the Agent.

## 5. Where FastMCP fits
**FastMCP** is the primary technology for implementing *custom* MCP servers. When our domain requires a new capability (e.g., connecting to Databricks safely), we will build a FastMCP server, rather than hardcoding Databricks clients directly into the platform runtime.

## 6. Authentication and Authorization
MCP is an integration boundary, NOT a security boundary.
* **Authentication:** Handled by the Platform Runtime prior to making MCP calls.
* **Authorization:** The deterministic Policy Engine evaluates the Agent's identity and intent *before* allowing the MCP request to proceed.

## 7. How MCP servers are classified and trusted
MCP servers must be explicitly declared in `mcp/` artifacts with trust boundaries (e.g., `TRUSTED_INTERNAL`, `UNTRUSTED_EXTERNAL`). The Policy Engine restricts what data can be sent to untrusted servers.

## 8. Evaluating external MCP servers
Before use, external MCP servers must undergo a security review, and their schemas must be statically validated against our platform's allowed actions list.

## 9. Preventing Data Leakage
The Policy Engine intercepts all data bound for an MCP server. It applies redaction rules (e.g., scrubbing PII or secrets) before the payload leaves the platform boundary.

## 10. Controlling read-only vs write capabilities
For the MVP, all allowed MCP capabilities are strictly READ ONLY. This is enforced deterministically by the Policy Engine, which will reject any tool invocation flagged as "WRITE" or "HIGH RISK" regardless of the LLM's justification.

## 11. Audit and Observability
Every MCP tool call (request payload, response payload, latency, success/failure) is logged deterministically by the Platform Runtime's observability layer, associating the call with the Agent ID and Session ID.

## 12. Exposing capabilities to Agents/Skills/Workflows
The Platform Runtime connects to the MCP servers, retrieves their tool definitions, and injects those schemas dynamically into the LLM's context window based on the active Agent's configuration.

## 13. Mock MCP servers in the MVP
To demonstrate the architecture safely, the MVP will utilize minimal FastMCP implementations that simulate domain systems (Hangfire, NiFi, Kafka, Databricks). These mocks will return deterministic, realistic READ ONLY evidence of replication failures or delays.

## 14. Evolving toward production
Future iterations will replace the mock FastMCP servers with production FastMCP servers connecting to real corporate networks. The core Platform Runtime will require zero changes, as it already respects the MCP contract.
