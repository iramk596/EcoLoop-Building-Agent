from typing import Dict, List

import pandas as pd

from app.config import SIMULATION_DIR


class EnergyPlusParser:
    """
    Parses the EnergyPlus HTML report (eplustbl.htm)
    and extracts key building performance metrics.
    """

    def __init__(self):
        self.report_path = SIMULATION_DIR / "eplustbl.htm"

    def report_exists(self) -> bool:
        return self.report_path.exists()

    def load_tables(self) -> List[pd.DataFrame]:
        """
        Load all HTML tables from the EnergyPlus report.
        """
        if not self.report_exists():
            raise FileNotFoundError(
                f"EnergyPlus report not found:\n{self.report_path}"
            )

        return pd.read_html(self.report_path)

    def extract_summary(self) -> Dict:
        """
        Extract key metrics from the EnergyPlus report.
        """

        tables = self.load_tables()

        summary = {
            "number_of_tables": len(tables),
            "report_file": str(self.report_path),
            "building_area_m2": None,
            "site_energy_gj": None,
            "net_site_energy_gj": None,
            "source_energy_gj": None,
            "electricity_gj": None,
            "heating_gj": None,
            "cooling_gj": None,
        }

        # -------------------------------------------------
        # TABLE 0 : Energy Summary
        # -------------------------------------------------
        try:
            table0 = tables[0]

            for _, row in table0.iterrows():

                name = str(row.iloc[0]).strip()

                if name == "Total Site Energy":
                    summary["site_energy_gj"] = row.iloc[1]

                elif name == "Net Site Energy":
                    summary["net_site_energy_gj"] = row.iloc[1]

                elif name == "Total Source Energy":
                    summary["source_energy_gj"] = row.iloc[1]

        except Exception:
            pass

        # -------------------------------------------------
        # TABLE 2 : Building Area
        # -------------------------------------------------
        try:
            table2 = tables[2]

            for _, row in table2.iterrows():

                name = str(row.iloc[0]).strip()

                if name == "Total Building Area":
                    summary["building_area_m2"] = row.iloc[1]

        except Exception:
            pass

        # -------------------------------------------------
        # TABLE 3 : End Uses
        # -------------------------------------------------
        try:
            table3 = tables[3]

            for _, row in table3.iterrows():

                name = str(row.iloc[0]).strip()

                if name == "Heating":
                    summary["heating_gj"] = row.iloc[1]

                elif name == "Cooling":
                    summary["cooling_gj"] = row.iloc[1]

                elif name == "Interior Lighting":
                    summary["electricity_gj"] = row.iloc[1]

        except Exception:
            pass

        return summary