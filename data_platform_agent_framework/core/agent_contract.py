from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from enum import Enum

class AgentPurpose(Enum):
    MONITORING = "MONITORING"
    INVESTIGATION = "INVESTIGATION"
    PROVISIONING = "PROVISIONING"
    QUALITY = "QUALITY"

@dataclass
class AgentContract:
    identity: str
    purpose: AgentPurpose
    domain: str
    capabilities: List[str] = field(default_factory=list)
    skills: List[str] = field(default_factory=list)
    workflows: List[str] = field(default_factory=list)
    tools: List[str] = field(default_factory=list)
    mcp_dependencies: List[str] = field(default_factory=list)
    permissions: List[str] = field(default_factory=list)
    policies: List[str] = field(default_factory=list)
    memory_config: Optional[Dict[str, Any]] = None
    configuration: Dict[str, Any] = field(default_factory=dict)

    def validate(self) -> bool:
        if not self.identity or not self.purpose or not self.domain:
            return False
        return True
