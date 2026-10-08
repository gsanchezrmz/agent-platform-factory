---
name: development-best-practices
description: "Procedural guide for developing robust Data Platform components, emphasizing testing, observability, and security."
when_to_use: "When writing, reviewing, or architecting new code for Data Platform components."
technologies: ["python", "csharp", "sql"]
dependencies:
  - "skills/development-best-practices/reference/python_best_practices.md"
  - "skills/development-best-practices/reference/csharp_best_practices.md"
  - "skills/development-best-practices/reference/sql_best_practices.md"
---

# Development Best Practices

## Overview
This Skill defines the universal procedure for developing Data Platform components. It ensures components are maintainable, secure, observable, and aligned with enterprise standards.

## Procedure

When tasked with writing or reviewing code, follow this lifecycle:

### 1. Requirements & Architecture Analysis
*   Do not immediately write code.
*   Determine the target programming language (Python, C#, or SQL).
*   **Mandatory Action:** Load the corresponding reference material from `skills/development-best-practices/reference/`.

### 2. Implementation Strategy
*   **Simplicity First:** Avoid over-engineering. Do not introduce microservices or complex async patterns unless explicitly justified by scale requirements.
*   **Configuration & Secrets:** Never hardcode secrets. Ensure configuration is injected via environment variables or secure key vaults, adhering to the language-specific reference.
*   **Error Handling:** Fail fast and loudly. Do not swallow exceptions.

### 3. Observability & Logging
*   All components must emit structured logs.
*   Ensure every logical transaction generates or passes a `CorrelationId`.
*   Distinguish between operational metrics (e.g., latency) and business metrics (e.g., rows processed).

### 4. Validation & Testing
*   Write unit tests for business logic.
*   Mock external dependencies (databases, APIs, MCP servers).
*   Consult the language reference for the required testing framework.

### 5. Self-Review
Before finalizing implementation, ask yourself:
*   Does this code handle nulls or network timeouts gracefully?
*   Are secrets exposed in logs or traces?
*   Is the dependency footprint as small as possible?
