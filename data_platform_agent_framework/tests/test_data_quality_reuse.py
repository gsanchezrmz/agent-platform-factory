from agents.data_quality.agent import DataQualityAgent
from security.policy_engine import PolicyEngine
from security.models import Identity
from core.observability import ObservabilityTracker

def test_data_quality_reuses_core():
    # Tests that the DQ agent works using the EXACT same policy engine and tracker
    engine = PolicyEngine()
    identity = Identity(user_id="system", roles=["operator"])
    agent = DataQualityAgent(identity, engine)
    tracker = ObservabilityTracker()

    result = agent.evaluate_quality("dbo.Users", tracker)

    assert result["status"] == "PASS"
    events = [e.event_type for e in tracker.get_events()]
    assert "DQ_CHECK_START" in events
    assert "POLICY_EVALUATION" in events
