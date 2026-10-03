# Component Model

- **Agent:** Interprets intent, uses tools, reasons. Cannot execute arbitrary commands or bypass policy.
- **Skill:** Domain heuristics and procedures (read-only knowledge).
- **Workflow:** Sequences of steps, evaluated by Policy Engine.
- **Tool:** Executable capability with specific risk and required permissions.
- **Policy Engine:** Deterministic rule evaluator outside the LLM.
- **MCP:** Standardized interface for external integrations.
