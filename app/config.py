from pathlib import Path
import os

from dotenv import load_dotenv

load_dotenv()


PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"
SIMULATION_DIR = DATA_DIR / "simulation"

SIMULATION_DIR.mkdir(parents=True, exist_ok=True)


ENERGYPLUS_PATH = os.getenv("ENERGYPLUS_PATH")
WEATHER_FILE = os.getenv("ENERGYPLUS_WEATHER")
IDF_FILE = os.getenv("ENERGYPLUS_IDF")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME", "llama-3.3-70b-versatile")