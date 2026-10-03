from typing import Dict, Any
from core.workflow import Workflow, WorkflowStep

def run_dq_check_step(ctx: Dict[str, Any]) -> Any:
    exec_tool = ctx["execute_tool"]
    success, result = exec_tool("run_dq_check", {"table": ctx["table"]})

    if not success:
        return {"status": "BLOCKED", "reason": result}

    if result.get("null_count", -1) == 0:
        return {"status": "PASS", "facts": result}
    else:
        return {"status": "FAIL", "facts": result}

def get_dq_workflow() -> Workflow:
    return Workflow(
        identity="evaluate_dq_workflow",
        description="Evaluates data quality for a table.",
        steps=[WorkflowStep(name="evaluate_quality", action=run_dq_check_step)]
    )
