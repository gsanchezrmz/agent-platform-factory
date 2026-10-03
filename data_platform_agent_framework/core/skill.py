from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Skill:
    identity: str
    description: str
    knowledge: str
    procedures: str
    heuristics: str

    def get_context(self) -> Dict[str, str]:
        """Provides the skill context to the agent runtime."""
        return {
            "knowledge": self.knowledge,
            "procedures": self.procedures,
            "heuristics": self.heuristics
        }
