from typing import Dict, Any, Tuple
from core.agent_contract import AgentContract, AgentPurpose
from core.observability import ObservabilityTracker
from security.policy_engine import PolicyEngine
from security.models import PolicyRequest, Identity
from integrations.mcp.adapters import get_replication_status_tool, get_bronze_pipeline_status_tool, get_restart_pipeline_tool
from integrations.mcp.mocks import MockMCPClient

class ReplicationMonitoringAgent:
    def __init__(self, identity: Identity, policy_engine: PolicyEngine):
        self.contract = AgentContract(
            identity="repl-monitor-001",
            purpose=AgentPurpose.INVESTIGATION,
            domain="DataPlatform",
            tools=["check_replication_status", "check_bronze_pipeline", "restart_bronze_pipeline"]
        )
        self.identity = identity
        self.policy_engine = policy_engine
        self.mcp_client = MockMCPClient()
        self.tools_map = {
            "check_replication_status": get_replication_status_tool(),
            "check_bronze_pipeline": get_bronze_pipeline_status_tool(),
            "restart_bronze_pipeline": get_restart_pipeline_tool()
        }

    def execute_tool_with_policy(self, tool_id: str, inputs: Dict[str, Any], tracker: ObservabilityTracker) -> Tuple[bool, Any]:
        tool = self.tools_map.get(tool_id)
        if not tool:
            return False, "Tool not found"

        req = PolicyRequest(
            identity=self.identity,
            agent_id=self.contract.identity,
            tool_identity=tool.identity,
            operation=tool.operation_type,
            resource=str(inputs),
            environment=tool.environment,
            risk=tool.risk
        )

        decision = self.policy_engine.evaluate(req)
        tracker.record_event("POLICY_EVALUATION", self.contract.identity, {"tool": tool_id, "decision": decision.allowed, "reason": decision.reason, "requires_approval": decision.requires_approval})

        if not decision.allowed:
            return False, f"Policy Denied: {decision.reason}"

        if decision.requires_approval:
            return False, "Action requires out-of-band human approval."

        # Execute tool via MCP
        try:
            result = self.mcp_client.execute_tool(tool_id, inputs)
            tracker.record_event("TOOL_EXECUTION", self.contract.identity, {"tool": tool_id, "status": "SUCCESS"})
            return True, result
        except Exception as e:
            tracker.record_event("TOOL_EXECUTION", self.contract.identity, {"tool": tool_id, "status": "ERROR", "error": str(e)})
            return False, str(e)

    def investigate(self, config_id: str, topic: str, tracker: ObservabilityTracker) -> Dict[str, Any]:
        """Simulates an LLM agent reasoning loop."""
        tracker.record_event("INVESTIGATION_START", self.contract.identity, {"config_id": config_id, "topic": topic})

        # Step 1: Agent decides to check replication status
        success, repl_result = self.execute_tool_with_policy("check_replication_status", {"config_id": config_id}, tracker)
        if not success:
            return {"diagnosis": "UNKNOWN", "reason": repl_result}

        # Step 2: Agent interprets result
        if repl_result.get("status") == "STOPPED":
            # Agent infers pipeline might be failing too, checks bronze
            tracker.record_event("AGENT_INFERENCE", self.contract.identity, {"inference": "Replication stopped, checking downstream pipeline"})

            s2, bronze_result = self.execute_tool_with_policy("check_bronze_pipeline", {"topic": topic}, tracker)

            if s2 and bronze_result.get("status") == "FAILED":
                # Agent concludes incident
                return {
                    "diagnosis": "INCIDENT",
                    "facts": {"replication": repl_result, "bronze": bronze_result},
                    "inference": "Pipeline failure caused upstream replication to halt."
                }

        return {
            "diagnosis": "HEALTHY",
            "facts": {"replication": repl_result}
        }
