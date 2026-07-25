from pathlib import Path
import subprocess

from app.config import (
    ENERGYPLUS_PATH,
    WEATHER_FILE,
    IDF_FILE,
    SIMULATION_DIR,
)


class EnergyPlusRunner:
    """
    Runs EnergyPlus simulations and stores all outputs
    inside data/simulation/.
    """

    def __init__(self):
        self.energyplus = ENERGYPLUS_PATH
        self.weather = WEATHER_FILE
        self.idf = IDF_FILE
        self.output_dir = SIMULATION_DIR

    def run(self):

        self.output_dir.mkdir(parents=True, exist_ok=True)

        command = [
            self.energyplus,
            "-w",
            self.weather,
            "-d",
            str(self.output_dir),
            self.idf,
        ]

        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
        )

        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "output_directory": str(self.output_dir),
        }