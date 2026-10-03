from dataclasses import dataclass
from typing import List, Dict, Any, Callable
from core.observability import ObservabilityTracker

@dataclass
class EvaluationScenario:
    name: str
    description: str
    input_state: Dict[str, Any]
    expected_outcome: Dict[str, Any]

@dataclass
class EvaluationResult:
    scenario_name: str
    passed: bool
    details: str

class EvaluationFramework:
    def __init__(self):
        self.scenarios: List[EvaluationScenario] = []

    def add_scenario(self, scenario: EvaluationScenario):
        self.scenarios.append(scenario)

    def run_evaluation(self, agent_runner: Callable[[Dict[str, Any], ObservabilityTracker], Any]) -> List[EvaluationResult]:
        results = []
        for scenario in self.scenarios:
            tracker = ObservabilityTracker()
            try:
                outcome = agent_runner(scenario.input_state, tracker)

                # Basic check: do outcome keys/values match expectations?
                passed = True
                details = []
                for k, v in scenario.expected_outcome.items():
                    if outcome.get(k) != v:
                        passed = False
                        details.append(f"Expected {k}={v}, got {outcome.get(k)}")

                results.append(EvaluationResult(
                    scenario_name=scenario.name,
                    passed=passed,
                    details=", ".join(details) if not passed else "Success"
                ))
            except Exception as e:
                results.append(EvaluationResult(
                    scenario_name=scenario.name,
                    passed=False,
                    details=f"Exception during execution: {str(e)}"
                ))
        return results
