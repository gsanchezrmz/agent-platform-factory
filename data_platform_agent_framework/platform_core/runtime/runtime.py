import yaml
import os
from typing import Dict, Any, Tuple
from platform_core.core.agent_contract import AgentContract, AgentPurpose
from platform_core.core.registry import Registry
from platform_core.core.tool import Tool, OperationType, RiskLevel
from platform_core.core.workflow import Workflow, WorkflowStep
from platform_core.core.skill import Skill
from platform_core.observability.observability import ObservabilityTracker
from platform_core.security.policy_engine import PolicyEngine
from platform_core.security.models import PolicyRequest, Identity
from platform_core.integrations.mcp.mocks import MockMCPClient

class AgentRuntime:
    """The reusable execution layer that evaluates policy and runs agent actions."""

    def __init__(self, policy_engine: PolicyEngine, artifacts_dir: str):
        self.policy_engine = policy_engine
        self.artifacts_dir = artifacts_dir
        self.tool_registry = Registry[Tool]()
        self.workflow_registry = Registry[Workflow]()
        self.skill_registry = Registry[Skill]()
        self.agent_registry = Registry[AgentContract]()
        self.tracker = ObservabilityTracker()
        self.mcp_client = MockMCPClient()

    def load_artifacts(self):
        """Loads declarative artifacts from the filesystem."""
        # Load agents
        agents_dir = os.path.join(self.artifacts_dir, 'agents')
        if os.path.exists(agents_dir):
            for file in os.listdir(agents_dir):
                if file.endswith('.yaml'):
                    with open(os.path.join(agents_dir, file), 'r') as f:
                        data = yaml.safe_load(f)
                        contract = AgentContract(
                            identity=data['identity'],
                            purpose=AgentPurpose(data['purpose']),
                            domain=data['domain'],
                            tools=data.get('tools', []),
                            workflows=data.get('workflows', []),
                            skills=data.get('skills', [])
                        )
                        self.agent_registry.register(contract.identity, contract)

        # In a full implementation, we would similarly dynamically load declarative workflows
        # mapping them to registered python callables, and load skills from markdown.
        # For this MVP step, we will load the Agent configs declaratively to prove the architecture.

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

        try:
            result = self.mcp_client.execute_tool(tool_id, inputs)
            self.tracker.record_event("TOOL_EXECUTION", contract.identity, {"tool": tool_id, "status": "SUCCESS"})
            return True, result
        except Exception as e:
            self.tracker.record_event("TOOL_EXECUTION", contract.identity, {"tool": tool_id, "status": "ERROR", "error": str(e)})
            return False, str(e)

    def execute_workflow(self, contract_id: str, identity: Identity, workflow_id: str, initial_state: Dict[str, Any]) -> Any:
        contract = self.agent_registry.get(contract_id)

        if workflow_id not in contract.workflows:
            raise ValueError(f"Workflow {workflow_id} not allowed by Agent Contract.")

        workflow = self.workflow_registry.get(workflow_id)

        runtime_context = initial_state.copy()
        runtime_context["agent_id"] = contract.identity
        runtime_context["identity"] = identity

        def secure_tool_executor(t_id: str, t_inputs: Dict[str, Any]):
            return self.execute_tool(contract, identity, t_id, t_inputs)

        runtime_context["execute_tool"] = secure_tool_executor

        return workflow.execute(runtime_context, self.tracker)
