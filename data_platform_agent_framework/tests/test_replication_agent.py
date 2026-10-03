from agents.replication_monitoring.agent import ReplicationMonitoringAgent
from security.policy_engine import PolicyEngine
from core.runtime import AgentRuntime
from security.models import Identity

def test_replication_investigation_loop():
    engine = PolicyEngine()
    runtime = AgentRuntime(engine)
    identity = Identity(user_id="system", roles=["operator"])
    agent = ReplicationMonitoringAgent(identity, runtime)

    # "config_456" is mock data for STOPPED replication, triggering bronze check.
    result = agent.investigate("config_456", "topic_B")

    assert result["diagnosis"] == "INCIDENT"
    assert "replication" in result["facts"]
    assert "bronze" in result["facts"]

    events = [e.event_type for e in runtime.tracker.get_events()]
    assert "WORKFLOW_START" in events
    assert "POLICY_EVALUATION" in events
    assert "TOOL_EXECUTION" in events
