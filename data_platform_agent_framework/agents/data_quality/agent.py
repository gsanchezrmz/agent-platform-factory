from typing import Dict, Any
from core.agent_contract import AgentContract, AgentPurpose
from core.runtime import AgentRuntime
from core.tool import Tool, OperationType, RiskLevel
from security.models import Identity
from .workflows import get_dq_workflow

def get_dq_check_tool() -> Tool:
    return Tool(
        identity="run_dq_check",
        description="Runs a data quality check on a table.",
        input_schema={"type": "object", "properties": {"table": {"type": "string"}}},
        output_schema={"type": "object", "properties": {"null_count": {"type": "integer"}}},
        operation_type=OperationType.READ,
        risk=RiskLevel.LOW,
        environment="PROD"
    )

class DataQualityAgent:
    def __init__(self, identity: Identity, runtime: AgentRuntime):
        self.identity = identity
        self.runtime = runtime

        self.contract = AgentContract(
            identity="dq-monitor-001",
            purpose=AgentPurpose.QUALITY,
            domain="DataPlatform",
            tools=["run_dq_check"],
            workflows=["evaluate_dq_workflow"]
        )

        self.runtime.tool_registry.register("run_dq_check", get_dq_check_tool())
        self.runtime.workflow_registry.register("evaluate_dq_workflow", get_dq_workflow())

    def evaluate_quality(self, table: str) -> Dict[str, Any]:
        initial_state = {"table": table}
        return self.runtime.execute_workflow(self.contract, self.identity, "evaluate_dq_workflow", initial_state)
