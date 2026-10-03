from agents.data_quality.agent import DataQualityAgent
from security.policy_engine import PolicyEngine
from core.runtime import AgentRuntime
from security.models import Identity

def test_data_quality_reuses_core():
    # Tests that the DQ agent works using the EXACT same policy engine and runtime
    engine = PolicyEngine()
    runtime = AgentRuntime(engine)
    identity = Identity(user_id="system", roles=["operator"])
    agent = DataQualityAgent(identity, runtime)

    result = agent.evaluate_quality("dbo.Users")

    assert result["status"] == "PASS"
    events = [e.event_type for e in runtime.tracker.get_events()]
    assert "WORKFLOW_START" in events
    assert "POLICY_EVALUATION" in events
    assert "TOOL_EXECUTION" in events
