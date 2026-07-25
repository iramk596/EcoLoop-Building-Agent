from pydantic import BaseModel


class BuildingState(BaseModel):
    """
    Represents the current state of the building.
    This object will be sent to the AI optimizer.
    """

    building_area_m2: float = 0.0

    site_energy_gj: float = 0.0

    electricity_gj: float = 0.0

    heating_gj: float = 0.0

    cooling_gj: float = 0.0

    occupancy: str = "Medium"

    outdoor_temperature: float = 32.0

    indoor_temperature: float = 24.0

    humidity: float = 55.0