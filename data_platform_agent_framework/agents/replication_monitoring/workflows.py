from typing import Dict, Any
from core.workflow import Workflow, WorkflowStep

def check_replication_step(ctx: Dict[str, Any]) -> Any:
    exec_tool = ctx["execute_tool"]
    config_id = ctx["config_id"]
    success, result = exec_tool("check_replication_status", {"config_id": config_id})
    if not success:
        return {"status": "ERROR", "reason": result}
    return result

def check_downstream_step(ctx: Dict[str, Any]) -> Any:
    exec_tool = ctx["execute_tool"]
    repl_result = ctx.get("check_replication")

    if repl_result and repl_result.get("status") == "STOPPED":
        success, bronze_result = exec_tool("check_bronze_pipeline", {"topic": ctx["topic"]})
        if success and bronze_result.get("status") == "FAILED":
            return {
                "diagnosis": "INCIDENT",
                "facts": {"replication": repl_result, "bronze": bronze_result},
                "inference": "Pipeline failure caused upstream replication to halt."
            }

    return {
        "diagnosis": "HEALTHY",
        "facts": {"replication": repl_result}
    }

def get_investigation_workflow() -> Workflow:
    return Workflow(
        identity="investigate_replication_workflow",
        description="Standard operating procedure for investigating a replication config.",
        steps=[
            WorkflowStep(name="check_replication", action=check_replication_step),
            WorkflowStep(name="check_downstream", action=check_downstream_step)
        ]
    )
