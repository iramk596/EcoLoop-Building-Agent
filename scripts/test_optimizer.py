from app.models.building_state import BuildingState
from app.services.optimizer import OptimizerService


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

optimizer = OptimizerService()

result = optimizer.optimize(building)

print()

print("Energy Efficiency Score:", result.energy_efficiency_score)

print("Priority Area:", result.priority_area)

print("Estimated Savings:", result.estimated_savings_percent, "%")

print("Estimated CO₂ Reduction:", result.estimated_co2_reduction_percent, "%")

print("Confidence:", result.confidence_score, "%")

print("\nRecommendations:\n")

for i, recommendation in enumerate(result.recommendations, start=1):
    print(f"{i}. {recommendation.title}")
    print(f"   {recommendation.description}")
    print()