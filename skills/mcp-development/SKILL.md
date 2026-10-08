---
name: mcp-development
description: "Procedural guide for designing, implementing, and securing Model Context Protocol (MCP) servers and tools."
when_to_use: "When an agent is tasked with building new infrastructure integrations or exposing domain capabilities to the LLM."
dependencies:
  - "skills/mcp-development/reference/mcp_best_practices.md"
  - "skills/mcp-development/reference/corporate-gateway.md"
---

# MCP Server Development Process

## Overview
This Skill defines the procedural workflow for creating robust MCP servers. It ensures that tools are discoverable, secure, and resilient when interacting with enterprise systems.

## Procedure

### 1. Capability Assessment
*   **Is MCP necessary?** Verify that the capability requires external system access or complex state management. Simple pure-logic functions should remain within the agent runtime.
*   **Identify Tools:** Define the exact boundary of what the MCP server will expose.

### 2. Schema Design & Naming
*   Design the Input/Output JSON schemas.
*   Tool names must be descriptive and follow the conventions defined in `reference/mcp_best_practices.md`.
*   Classify every tool explicitly as `READ` or `WRITE`.

### 3. Security & Gateway Validation
*   Load `reference/corporate-gateway.md`.
*   Determine the authentication mechanism required by the target enterprise system.
*   Determine the network boundary (e.g., does this require a proxy or TLS certificate?).
*   Apply the Principle of Least Privilege to the MCP server's IAM role.

### 4. Implementation
*   Delegate coding tasks to the `development-best-practices` skill based on the chosen language (e.g., Python FastMCP).
*   Implement strict validation on all input parameters to prevent injection or malicious payloads.
*   Ensure all errors are caught and returned gracefully as structured tool responses, rather than crashing the server.

### 5. Testing & Observability
*   Write unit tests simulating the LLM client payloads.
*   Ensure the MCP server logs all incoming requests (scrubbing PII/secrets) to assist in pipeline debugging.
