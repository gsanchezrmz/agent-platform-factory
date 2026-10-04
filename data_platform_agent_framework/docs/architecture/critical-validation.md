# Critical Validation

## Question 1: Where exactly would I add a new Data Quality Agent's components?
If building a new Data Quality Agent, you would add files here:

- **Agent Definition:** `artifacts/agents/data_quality.yaml`
- **Skills:** `artifacts/skills/data_profiling.md`
- **Workflows:** `artifacts/workflows/evaluate_dq.yaml`
- **Policies:** Add rules to `artifacts/policies/dq_rules.yaml` (or update Python Engine if logic changes).
- **Tools:** Create Python executable capabilities in `domain/tools/dq_tools.py` and wrap via FastMCP.
- **Evaluation:** Add scenarios to `artifacts/evaluations/dq_scenarios.yaml`.

## Question 2: Which parts of the repository would NOT need to change?
The entire `platform/` directory remains untouched. This includes:
- `platform/runtime/` (Agent Runtime orchestrator)
- `platform/security/` (Policy Engine, Role validation)
- `platform/core/` (Interfaces and Registries for parsing YAML into domain objects)
- `platform/observability/` (Execution tracker)

This proves the architecture is a reusable Agent Engineering Platform, rather than a monolithic application containing a single agent.
