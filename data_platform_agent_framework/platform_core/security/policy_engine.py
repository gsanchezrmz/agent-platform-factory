from platform_core.security.models import PolicyRequest, PolicyDecision, ApprovalStatus
from platform_core.core.tool import OperationType, RiskLevel

class PolicyEngine:
    def __init__(self):
        self.allowed_environments_by_role = {
            "admin": ["DEV", "TEST", "PROD"],
            "operator": ["DEV", "TEST", "PROD"],
            "viewer": ["DEV", "TEST", "PROD"]
        }

    def evaluate(self, request: PolicyRequest) -> PolicyDecision:
        can_access_env = False
        for role in request.identity.roles:
            if request.environment in self.allowed_environments_by_role.get(role, []):
                can_access_env = True
                break

        if not can_access_env:
            return PolicyDecision(allowed=False, reason="Environment not allowed for user roles.", requires_approval=False)

        if request.operation in [OperationType.WRITE, OperationType.DELETE, OperationType.EXECUTE]:
            if "viewer" in request.identity.roles and "admin" not in request.identity.roles and "operator" not in request.identity.roles:
                return PolicyDecision(allowed=False, reason="Role does not permit mutating operations.", requires_approval=False)

            if request.environment == "PROD" and request.risk in [RiskLevel.HIGH, RiskLevel.CRITICAL]:
                return PolicyDecision(allowed=False, reason="High risk operations in PROD require human approval.", requires_approval=True, approval_status=ApprovalStatus.PENDING)

        return PolicyDecision(allowed=True, reason="Policy satisfied.", requires_approval=False, approval_status=ApprovalStatus.NOT_REQUIRED)
