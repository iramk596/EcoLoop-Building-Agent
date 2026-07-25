from typing import List

from pydantic import BaseModel, Field


class Recommendation(BaseModel):
    """
    Represents a single AI optimization recommendation.
    """

    title: str = Field(..., description="Recommendation title")

    description: str = Field(..., description="Detailed explanation")

    priority: str = Field(
        ...,
        description="Priority level (High, Medium, Low)"
    )

    impact_percent: float = Field(
        ...,
        description="Estimated contribution to energy savings"
    )


class OptimizationResult(BaseModel):
    """
    Complete AI optimization response.
    """

    energy_efficiency_score: int = Field(
        ...,
        ge=0,
        le=100
    )

    priority_area: str

    estimated_savings_percent: float

    estimated_co2_reduction_percent: float

    confidence_score: int = Field(
        ...,
        ge=0,
        le=100
    )

    recommendations: List[Recommendation]