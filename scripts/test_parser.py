from app.energyplus.parser import EnergyPlusParser
import pandas as pd

# Show ALL columns
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)

parser = EnergyPlusParser()

tables = parser.load_tables()

print("TABLE 0")
print("=" * 100)
print(tables[0])

print("\n\nTABLE 2")
print("=" * 100)
print(tables[2])

print("\n\nTABLE 3")
print("=" * 100)
print(tables[3])