from typing import Dict, Any, Tuple
from core.agent_contract import AgentContract
from core.registry import Registry
from core.tool import Tool
from core.workflow import Workflow
from core.skill import Skill
from core.observability import ObservabilityTracker
from security.policy_engine import PolicyEngine
from security.models import PolicyRequest, Identity
from integrations.mcp.mocks import MockMCPClient # In real app, this is a generic MCP dispatcher

class AgentRuntime:
    """The reusable execution layer that evaluates policy and runs agent actions."""

    def __init__(self, policy_engine: PolicyEngine):
        self.policy_engine = policy_engine
        self.tool_registry = Registry[Tool]()
        self.workflow_registry = Registry[Workflow]()
        self.skill_registry = Registry[Skill]()
        self.tracker = ObservabilityTracker()
        self.mcp_client = MockMCPClient() # Simulates routing to FastMCP servers

    def execute_tool(self, contract: AgentContract, identity: Identity, tool_id: str, inputs: Dict[str, Any]) -> Tuple[bool, Any]:
        if tool_id not in contract.tools:
            return False, f"Tool {tool_id} not allowed by Agent Contract."

        tool = self.tool_registry.get(tool_id)

        req = PolicyRequest(
            identity=identity,
            agent_id=contract.identity,
            tool_identity=tool.identity,
            operation=tool.operation_type,
            resource=str(inputs),
            environment=tool.environment,
            risk=tool.risk
        )

        decision = self.policy_engine.evaluate(req)
        self.tracker.record_event("POLICY_EVALUATION", contract.identity, {"tool": tool_id, "allowed": decision.allowed, "reason": decision.reason})

        if not decision.allowed:
            return False, f"Policy Denied: {decision.reason}"

        if decision.requires_approval:
            return False, "Action requires out-of-band human approval."

        try:
            result = self.mcp_client.execute_tool(tool_id, inputs)
            self.tracker.record_event("TOOL_EXECUTION", contract.identity, {"tool": tool_id, "status": "SUCCESS"})
            return True, result
        except Exception as e:
            self.tracker.record_event("TOOL_EXECUTION", contract.identity, {"tool": tool_id, "status": "ERROR", "error": str(e)})
            return False, str(e)

    def execute_workflow(self, contract: AgentContract, identity: Identity, workflow_id: str, initial_state: Dict[str, Any]) -> Any:
        if workflow_id not in contract.workflows:
            raise ValueError(f"Workflow {workflow_id} not allowed by Agent Contract.")

        workflow = self.workflow_registry.get(workflow_id)

        # Inject platform capabilities into workflow context
        runtime_context = initial_state.copy()
        runtime_context["agent_id"] = contract.identity
        runtime_context["identity"] = identity

        # Expose a secure tool execution callback to the workflow
        def secure_tool_executor(t_id: str, t_inputs: Dict[str, Any]):
            return self.execute_tool(contract, identity, t_id, t_inputs)

        runtime_context["execute_tool"] = secure_tool_executor

        return workflow.execute(runtime_context, self.tracker)
