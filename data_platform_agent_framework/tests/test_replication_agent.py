import os
from platform_core.security.policy_engine import PolicyEngine
from platform_core.runtime import AgentRuntime
from platform_core.security.models import Identity
from domain.tools.replication_tools import get_replication_status_tool, get_bronze_pipeline_status_tool, get_restart_pipeline_tool
from domain.workflows.replication_workflows import get_investigation_workflow

def test_replication_investigation_loop():
    engine = PolicyEngine()
    artifacts_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'artifacts')
    runtime = AgentRuntime(engine, artifacts_dir)

    # Register Domain logic
    runtime.tool_registry.register("check_replication_status", get_replication_status_tool())
    runtime.tool_registry.register("check_bronze_pipeline", get_bronze_pipeline_status_tool())
    runtime.tool_registry.register("restart_bronze_pipeline", get_restart_pipeline_tool())
    runtime.workflow_registry.register("investigate_replication_workflow", get_investigation_workflow())

    # Load Declarative Agents
    runtime.load_artifacts()

    identity = Identity(user_id="system", roles=["operator"])

    # Run loop
    initial_state = {"config_id": "config_456", "topic": "topic_B"}
    result = runtime.execute_workflow("repl-monitor-001", identity, "investigate_replication_workflow", initial_state)

    assert result["diagnosis"] == "INCIDENT"
    assert "replication" in result["facts"]
    assert "bronze" in result["facts"]

    events = [e.event_type for e in runtime.tracker.get_events()]
    assert "WORKFLOW_START" in events
    assert "POLICY_EVALUATION" in events
    assert "TOOL_EXECUTION" in events
