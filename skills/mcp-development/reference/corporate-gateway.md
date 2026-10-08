# MCP Corporate Gateway Constraints

This reference details the security and networking requirements for deploying MCP servers within the Enterprise Corporate Gateway.

## 1. Network Boundaries
*   MCP servers must never expose public internet endpoints.
*   If an MCP server needs to reach an external SaaS (e.g., Jira, GitHub), it MUST route traffic through the designated Corporate Egress Proxy.
*   Direct database connections (e.g., to internal SQL clusters) are permitted only if the MCP server is deployed within the trusted VPC subnet.

## 2. Authentication & Authorization
*   **Client to Server:** The Platform Runtime must authenticate with the MCP Server using short-lived tokens (e.g., JWT) signed by the internal Identity Provider.
*   **Server to Target:** The MCP Server must authenticate to backend systems (e.g., Databricks) using Managed Identities or Service Principals. User-delegated credentials are prohibited for automated agents.

## 3. Secret Management
*   Secrets (API keys, connection strings) must be injected at runtime via the Enterprise Key Vault.
*   MCP Tool Inputs must never require the LLM to pass a secret. The secret must reside securely within the MCP server's environment.

## 4. TLS & Certificates
*   All communication over HTTP/SSE must use TLS 1.2 or higher.
*   Internal servers must use certificates signed by the Corporate Internal CA. Disable strict SSL validation only in local development environments.

## 5. Data Leakage Prevention & Auditing
*   MCP servers must scrub sensitive PII or PCI data before returning payloads to the LLM context.
*   All Tool executions must generate an audit log containing: Timestamp, Client ID, Tool Name, and Execution Status. Do NOT log the raw payload contents if they contain customer data.

## 6. Rate Limiting & Timeouts
*   MCP servers must enforce strict timeouts (e.g., 10 seconds max) to prevent hanging the LLM inference loop.
*   Implement rate limiting to prevent an autonomous agent loop from accidentally DDoS-ing an internal database.
