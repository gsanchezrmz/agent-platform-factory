import os
from platform_core.security.policy_engine import PolicyEngine
from platform_core.runtime import AgentRuntime
from platform_core.security.models import Identity
from domain.tools.dq_tools import get_dq_check_tool
from domain.workflows.dq_workflows import get_dq_workflow

def test_data_quality_reuses_core():
    engine = PolicyEngine()
    artifacts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'artifacts')
    runtime = AgentRuntime(engine, artifacts_dir)

    # Register Domain logic
    runtime.tool_registry.register("run_dq_check", get_dq_check_tool())
    runtime.workflow_registry.register("evaluate_dq_workflow", get_dq_workflow())

    # Load Declarative Agents
    runtime.load_artifacts()

    identity = Identity(user_id="system", roles=["operator"])

    initial_state = {"table": "dbo.Users"}
    result = runtime.execute_workflow("dq-monitor-001", identity, "evaluate_dq_workflow", initial_state)

    assert result["status"] == "PASS"
    events = [e.event_type for e in runtime.tracker.get_events()]
    assert "WORKFLOW_START" in events
    assert "POLICY_EVALUATION" in events
    assert "TOOL_EXECUTION" in events
