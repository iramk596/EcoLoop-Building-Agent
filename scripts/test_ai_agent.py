from app.agents.ai_agent import AIAgent
from app.models.building_state import BuildingState

agent = AIAgent()

building = BuildingState(
    building_area_m2=500,
    site_energy_gj=350,
    electricity_gj=180,
    heating_gj=40,
    cooling_gj=120,
    occupancy="High",
    outdoor_temperature=36,
    indoor_temperature=24,
    humidity=58,
)

result = agent.optimize(building)

print()

print("Energy Score:")
print(result.energy_efficiency_score)

print()

print("Priority:")
print(result.priority_area)

print()

print("Savings:")
print(result.estimated_savings_percent)

print()

print("CO2 Reduction:")
print(result.estimated_co2_reduction_percent)

print()

print("Confidence:")
print(result.confidence_score)

print()

print("Recommendations")

for rec in result.recommendations:
    print(f"- {rec.title}")
    print(f"  {rec.description}")