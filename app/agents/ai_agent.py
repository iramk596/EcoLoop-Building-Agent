import json

from groq import Groq

from app.config import GROQ_API_KEY, MODEL_NAME
from app.models.building_state import BuildingState
from app.models.optimization_result import OptimizationResult


class AIAgent:
    """
    Handles communication with the Groq LLM.
    """

    def __init__(self):

        if not GROQ_API_KEY:
            raise ValueError("Groq API key not found.")

        self.client = Groq(api_key=GROQ_API_KEY)

        self.model = MODEL_NAME

    def test_connection(self) -> str:
        """
        Simple connectivity test.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": "Say hello in one short sentence."
                }
            ]
        )

        return response.choices[0].message.content

    def optimize(self, building: BuildingState) -> OptimizationResult:
        """
        Analyze the building and return structured optimization advice.
        """

        prompt = f"""
You are an AI energy optimization expert for smart commercial buildings.

Analyze this building.

Building Area:
{building.building_area_m2} m²

Site Energy:
{building.site_energy_gj} GJ

Electricity Usage:
{building.electricity_gj} GJ

Heating Usage:
{building.heating_gj} GJ

Cooling Usage:
{building.cooling_gj} GJ

Indoor Temperature:
{building.indoor_temperature} °C

Outdoor Temperature:
{building.outdoor_temperature} °C

Humidity:
{building.humidity} %

Occupancy:
{building.occupancy}

Return ONLY valid JSON.

The JSON MUST exactly match this schema.

{{
    "energy_efficiency_score": 0,
    "priority_area": "",
    "estimated_savings_percent": 0,
    "estimated_co2_reduction_percent": 0,
    "confidence_score": 0,
    "recommendations": [
        {{
            "title": "",
            "priority": "",
            "impact_percent": 0,
            "description": ""
        }},
        {{
            "title": "",
            "priority": "",
            "impact_percent": 0,
            "description": ""
        }},
        {{
            "title": "",
            "priority": "",
            "impact_percent": 0,
            "description": ""
        }}
    ]
}}

Rules:

- Return ONLY JSON.
- Do NOT use markdown.
- Do NOT use ```json.
- Do NOT explain anything.
- Return exactly three recommendations.
- energy_efficiency_score must be between 0 and 100.
- confidence_score must be between 0 and 100.
- estimated_savings_percent must be numeric.
- estimated_co2_reduction_percent must be numeric.

For every recommendation include:

title

priority
(one of High, Medium, Low)

impact_percent
(estimated contribution to overall savings)

description

Make recommendations practical for a commercial office building.
"""

        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0.2,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
        )

        content = response.choices[0].message.content.strip()

        # Remove markdown fences if the model accidentally returns them
        if content.startswith("```"):
            content = (
                content
                .replace("```json", "")
                .replace("```", "")
                .strip()
            )

        try:
            data = json.loads(content)

        except json.JSONDecodeError as e:
            raise ValueError(
                f"Failed to parse JSON returned by Groq.\n\nResponse was:\n{content}"
            ) from e

        return OptimizationResult(**data)