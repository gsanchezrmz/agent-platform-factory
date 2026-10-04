from enum import Enum
from dataclasses import dataclass, field
from typing import Dict, Any, List

class MCPTrustLevel(Enum):
    APPROVED = "APPROVED"
    CONDITIONALLY_APPROVED = "CONDITIONALLY_APPROVED"
    REJECTED = "REJECTED"
    BLOCKED = "BLOCKED"

@dataclass
class MCP:
    name: str
    trust_level: MCPTrustLevel
    tools: List[str] = field(default_factory=list)
    configuration: Dict[str, Any] = field(default_factory=dict)

    def is_executable(self) -> bool:
        return self.trust_level in [MCPTrustLevel.APPROVED, MCPTrustLevel.CONDITIONALLY_APPROVED]
