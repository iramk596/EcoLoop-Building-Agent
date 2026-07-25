from fastapi import APIRouter

from app.models.building_state import BuildingState
from app.models.optimization_result import OptimizationResult
from app.services.optimizer import OptimizerService

router = APIRouter()

optimizer = OptimizerService()


@router.get("/")
def root():
    """
    Root endpoint.
    """
    return {
        "message": "Welcome to EcoLoop Building Agent API"
    }


@router.get("/health")
def health():
    """
    Health check endpoint.
    """
    return {
        "status": "healthy"
    }


@router.post(
    "/optimize",
    response_model=OptimizationResult
)
def optimize(building: BuildingState):
    """
    Optimize a building using AI.
    """

    result = optimizer.optimize(building)

    return result