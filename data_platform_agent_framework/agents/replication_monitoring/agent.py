from core.agent_contract import AgentContract, AgentPurpose
from core.runtime import AgentRuntime
from security.models import Identity
from typing import Dict, Any
from .skills import get_replication_investigation_skill
from .workflows import get_investigation_workflow
from integrations.mcp.adapters import get_replication_status_tool, get_bronze_pipeline_status_tool, get_restart_pipeline_tool

class ReplicationMonitoringAgent:
    """
    Domain-specific agent.
    It does not contain platform orchestration or policy checks.
    It registers its capabilities with the Runtime and invokes it.
    """
    def __init__(self, identity: Identity, runtime: AgentRuntime):
        self.identity = identity
        self.runtime = runtime

        self.contract = AgentContract(
            identity="repl-monitor-001",
            purpose=AgentPurpose.INVESTIGATION,
            domain="DataPlatform",
            tools=["check_replication_status", "check_bronze_pipeline", "restart_bronze_pipeline"],
            skills=["replication_investigation"],
            workflows=["investigate_replication_workflow"]
        )

        # Register domain specific components into the platform runtime
        self.runtime.tool_registry.register("check_replication_status", get_replication_status_tool())
        self.runtime.tool_registry.register("check_bronze_pipeline", get_bronze_pipeline_status_tool())
        self.runtime.tool_registry.register("restart_bronze_pipeline", get_restart_pipeline_tool())
        self.runtime.skill_registry.register("replication_investigation", get_replication_investigation_skill())
        self.runtime.workflow_registry.register("investigate_replication_workflow", get_investigation_workflow())

    def investigate(self, config_id: str, topic: str) -> Dict[str, Any]:
        initial_state = {"config_id": config_id, "topic": topic}
        # Delegate entirely to the platform Runtime to execute the workflow
        return self.runtime.execute_workflow(self.contract, self.identity, "investigate_replication_workflow", initial_state)
