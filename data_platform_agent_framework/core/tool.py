from dataclasses import dataclass, field
from typing import Dict, Any, Optional
from enum import Enum

class OperationType(Enum):
    READ = "READ"
    WRITE = "WRITE"
    DELETE = "DELETE"
    EXECUTE = "EXECUTE"
    ADMIN = "ADMIN"

class RiskLevel(Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"

@dataclass
class Tool:
    identity: str
    description: str
    input_schema: Dict[str, Any]
    output_schema: Dict[str, Any]
    operation_type: OperationType
    risk: RiskLevel
    required_permissions: list[str] = field(default_factory=list)
    resources: list[str] = field(default_factory=list)
    environment: str = "DEV"
    audit_requirements: str = "STANDARD"
