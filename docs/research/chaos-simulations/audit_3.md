# Iteration 3 Audit

**Simulated Architect Proposal:**
- Agent: `databricks-investigator`
- Tools: `get_databricks_logs`, `get_pipeline_state`
- Logic: Read logs. Find `AccessDeniedException`. Infer that the Databricks table ACLs are misconfigured.

**Red Teaming (Reviewer):**
The Architect fell into the "Tunnel Vision" trap. It assumed that because the error appeared in Databricks, Databricks was the root cause. It completely ignored external dependencies (IAM, Networking, DNS). The E2E topology map must explicitly mandate mapping external dependency graphs, not just internal pipeline components.

**Patch Required:**
Update `e2e-topology-template.md` to include a 4th dimension: `External Dependencies (IAM, DNS, Secrets)`. Update the Architect skill to require proposing Tools to verify these external dependencies.
