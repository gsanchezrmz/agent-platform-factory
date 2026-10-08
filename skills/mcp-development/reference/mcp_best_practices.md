# MCP Engineering Best Practices

This reference provides detailed technical knowledge for designing high-quality Model Context Protocol tools.

## 1. Tool Naming Conventions
*   Names must clearly indicate the domain, action, and target resource.
*   Use `snake_case` (e.g., `github_create_issue`, `databricks_get_pipeline_status`).
*   Avoid ambiguous verbs like `do`, `process`, or `run`. Use `get`, `create`, `update`, `delete`, `analyze`.

## 2. Input Schema Design
*   Schemas must be strictly typed using JSON Schema standards.
*   Provide clear `description` fields for every parameter. LLMs use these descriptions to understand how to formulate the tool call.
*   Mark mandatory fields explicitly in the `required` array.
*   Use `enum` where parameters have a fixed set of valid values to prevent LLM hallucinations.

## 3. Output Schema & Formatting
*   Return data in a format optimized for LLM comprehension (e.g., Markdown or structured JSON).
*   **Pagination:** If a tool queries a database or API that can return thousands of records, implement pagination (e.g., `limit`, `offset` parameters) and warn the LLM if the result set was truncated.

## 4. Error Handling
*   An MCP server should rarely crash. Unhandled exceptions break the LLM's reasoning loop.
*   Catch exceptions and return them in the tool output as a formatted string (e.g., `{"status": "error", "message": "Connection timeout to Database X"}`). This allows the LLM to read the error and formulate a retry or alternative strategy.

## 5. Transport Protocols
*   Use `stdio` transport for local, tightly coupled sidecar servers.
*   Use `SSE` (Server-Sent Events) or standard HTTP for remote servers operating across the network boundary.
