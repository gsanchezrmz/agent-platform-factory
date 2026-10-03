import pytest
from security.policy_engine import PolicyEngine
from security.models import PolicyRequest, Identity, ApprovalStatus
from core.tool import OperationType, RiskLevel

def test_viewer_denied_write():
    engine = PolicyEngine()
    req = PolicyRequest(
        identity=Identity(user_id="u1", roles=["viewer"]),
        agent_id="a1",
        tool_identity="restart_pipeline",
        operation=OperationType.EXECUTE,
        resource="pipeline_1",
        environment="DEV",
        risk=RiskLevel.MEDIUM
    )
    decision = engine.evaluate(req)
    assert not decision.allowed
    assert "mutating operations" in decision.reason.lower()

def test_admin_requires_approval_high_risk_prod():
    engine = PolicyEngine()
    req = PolicyRequest(
        identity=Identity(user_id="u1", roles=["admin"]),
        agent_id="a1",
        tool_identity="restart_pipeline",
        operation=OperationType.EXECUTE,
        resource="pipeline_1",
        environment="PROD",
        risk=RiskLevel.HIGH
    )
    decision = engine.evaluate(req)
    assert not decision.allowed
    assert decision.requires_approval
    assert decision.approval_status == ApprovalStatus.PENDING
