from agents.replication_monitoring.agent import ReplicationMonitoringAgent
from security.policy_engine import PolicyEngine
from security.models import Identity
from core.observability import ObservabilityTracker

def test_replication_investigation_loop():
    engine = PolicyEngine()
    identity = Identity(user_id="system", roles=["operator"])
    agent = ReplicationMonitoringAgent(identity, engine)
    tracker = ObservabilityTracker()

    # "config_456" is mock data for STOPPED replication, triggering bronze check.
    result = agent.investigate("config_456", "topic_B", tracker)

    assert result["diagnosis"] == "INCIDENT"
    assert "replication" in result["facts"]
    assert "bronze" in result["facts"]

    events = [e.event_type for e in tracker.get_events()]
    assert "POLICY_EVALUATION" in events
    assert "AGENT_INFERENCE" in events
