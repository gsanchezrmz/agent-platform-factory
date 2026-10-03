from dataclasses import dataclass
from typing import List, Optional
from enum import Enum
from core.tool import OperationType, RiskLevel

class ApprovalStatus(Enum):
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    DENIED = "DENIED"
    NOT_REQUIRED = "NOT_REQUIRED"

@dataclass
class Identity:
    user_id: str
    roles: List[str]

@dataclass
class PolicyRequest:
    identity: Identity
    agent_id: str
    tool_identity: str
    operation: OperationType
    resource: str
    environment: str
    risk: RiskLevel

@dataclass
class PolicyDecision:
    allowed: bool
    reason: str
    requires_approval: bool
    approval_status: ApprovalStatus = ApprovalStatus.NOT_REQUIRED
