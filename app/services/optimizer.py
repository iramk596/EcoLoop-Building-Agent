from app.agents.ai_agent import AIAgent
from app.models.building_state import BuildingState
from app.models.optimization_result import OptimizationResult


class OptimizerService:
    """
    Coordinates the complete building optimization workflow.

    Workflow:
    1. Receive building data.
    2. Send it to the AI agent.
    3. Return the optimization result.
    """

    def __init__(self):
        self.ai_agent = AIAgent()

    def optimize(self, building_state: BuildingState) -> OptimizationResult:
        """
        Optimize a building using AI.

        Args:
            building_state: Current state of the building.

        Returns:
            OptimizationResult
        """

        result = self.ai_agent.optimize(building_state)

        return result