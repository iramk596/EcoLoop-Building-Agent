import requests
from pathlib import Path

import plotly.graph_objects as go
import streamlit as st

API_BASE_URL = "http://13.127.83.53:8000"


# -------------------------
# Styling
# -------------------------
def load_custom_css():
    css_path = Path(__file__).parent / "styles" / "style.css"

    if css_path.exists():
        with open(css_path, "r", encoding="utf-8") as css:
            st.markdown(
                f"<style>{css.read()}</style>",
                unsafe_allow_html=True,
            )


# -------------------------
# Backend
# -------------------------
def optimize_building(payload):
    response = requests.post(
        f"{API_BASE_URL}/optimize",
        json=payload,
        timeout=30,
    )

    response.raise_for_status()

    return response.json()


# -------------------------
# Status Badges
# -------------------------
def render_status_badges(backend_online=True):

    badges = [
        (
            "🟢 FastAPI Connected"
            if backend_online
            else "🔴 Backend Offline",
            "#dcfce7" if backend_online else "#fee2e2",
            "#166534" if backend_online else "#991b1b",
        ),
        (
            "🤖 Groq AI Ready",
            "#eef2ff",
            "#1e3a8a",
        ),
        (
            "⚡ EnergyPlus Ready",
            "#fff7ed",
            "#9a3412",
        ),
    ]

    cols = st.columns(3)

    for col, (text, bg, color) in zip(cols, badges):

        col.markdown(
            f"""
            <div style="
                background:{bg};
                color:{color};
                padding:10px;
                text-align:center;
                border-radius:999px;
                font-weight:600;
                margin-bottom:15px;
            ">
            {text}
            </div>
            """,
            unsafe_allow_html=True,
        )


# -------------------------
# KPI Cards
# -------------------------
def render_kpi_cards(result):

    score = "--"
    savings = "--"
    co2 = "--"
    confidence = "--"

    if result:

        score = result.get("energy_efficiency_score", "--")

        if result.get("estimated_savings_percent") is not None:
            savings = f'{result["estimated_savings_percent"]:.1f}%'

        if result.get("estimated_co2_reduction_percent") is not None:
            co2 = f'{result["estimated_co2_reduction_percent"]:.1f}%'

        if result.get("confidence_score") is not None:
            confidence = f'{result["confidence_score"]}%'

    cards = [

        ("", "Energy Score", score),

        ("", "Estimated Savings", savings),

        ("", "CO₂ Reduction", co2),

        ("", "Confidence", confidence),

    ]

    cols = st.columns(4)

    for col, (icon, title, value) in zip(cols, cards):

        col.markdown(
            f"""
            <div style="
                background:white;
                border-radius:18px;
                padding:24px;
                box-shadow:0 10px 20px rgba(0,0,0,.06);
                text-align:center;
            ">

            <div style="
                font-size:18px;
                color:#64748b;
            ">
            {icon} {title}
            </div>

            <div style="
                margin-top:10px;
                font-size:34px;
                font-weight:700;
                color:#0f172a;
            ">
            {value}
            </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


# -------------------------
# Charts
# -------------------------
def build_energy_chart(
    electricity,
    heating,
    cooling,
):

    fig = go.Figure()

    fig.add_trace(
        go.Bar(
            x=[
                "Electricity",
                "Heating",
                "Cooling",
            ],
            y=[
                electricity,
                heating,
                cooling,
            ],
            text=[
                electricity,
                heating,
                cooling,
            ],
            textposition="outside",
        )
    )

    fig.update_layout(

        template="plotly_white",

        height=420,

        title="Building Energy Consumption",

        xaxis_title="Category",

        yaxis_title="Energy (GJ)",

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig


def build_savings_chart(result):

    total = 0

    if result:
        total = result.get(
            "estimated_savings_percent",
            0,
        )

    labels = [

        "Cooling",

        "Lighting",

        "HVAC",

        "Equipment",

    ]

    values = [

        total * 0.35,

        total * 0.25,

        total * 0.25,

        total * 0.15,

    ]

    fig = go.Figure(
        data=[
            go.Pie(
                labels=labels,
                values=values,
                hole=0.45,
            )
        ]
    )

    fig.update_layout(

        title="Estimated Savings Distribution",

        height=420,

        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20,
        ),
    )

    return fig


# -------------------------
# Recommendation Cards
# -------------------------
def render_recommendation_cards(result):

    st.subheader(" AI Recommendations")

    if not result:

        st.info("Run optimization to generate recommendations.")

        return

    recommendations = result.get(
        "recommendations",
        [],
    )

    for rec in recommendations:

        priority = rec.get(
            "priority",
            "Medium",
        )

        impact = rec.get(
            "impact_percent",
            0,
        )

        color = {

            "High": "#ef4444",

            "Medium": "#f59e0b",

            "Low": "#22c55e",

        }.get(priority, "#64748b")

        st.markdown(
            f"""
<div style="
background:white;
padding:22px;
margin-bottom:20px;
border-radius:18px;
border-left:8px solid {color};
box-shadow:0 8px 18px rgba(0,0,0,.06);
">

<h4>
 {rec.get("title")}
</h4>

<div style="margin-bottom:12px;">

<span style="
background:{color};
color:white;
padding:5px 10px;
border-radius:20px;
font-size:13px;
font-weight:bold;
">

{priority}

</span>

<span style="
margin-left:12px;
font-weight:600;
color:#2563eb;
">

Expected Saving:
{impact}%

</span>

</div>

<div style="
color:#475569;
line-height:1.6;
">

{rec.get("description")}

</div>

</div>
""",
            unsafe_allow_html=True,
        )


# -------------------------
# Main
# -------------------------
def main():

    st.set_page_config(
        page_title="EcoLoop Building Agent",
        page_icon="🏢",
        layout="wide",
    )

    load_custom_css()

    # -----------------------------
    # Session State Initialization
    # -----------------------------
    if "optimization_result" not in st.session_state:
        st.session_state["optimization_result"] = None

    if "backend_online" not in st.session_state:
        st.session_state["backend_online"] = True

    # -----------------------------
    # Header
    # -----------------------------
    st.title("🏢 EcoLoop Building Agent")

    st.markdown(
        """
        AI-powered building energy optimization using
        **EnergyPlus simulation, Groq LLM, and FastAPI**
        """
    )

    render_status_badges(st.session_state["backend_online"])

    st.divider()

    # -----------------------------
    # Sidebar
    # -----------------------------
    st.sidebar.header("🏢 Building Inputs")

    building_area = st.sidebar.number_input(
        "Building Area (m²)",
        value=1200.0,
        min_value=0.0,
    )

    site_energy = st.sidebar.number_input(
        "Site Energy (GJ)",
        value=180.0,
        min_value=0.0,
    )

    electricity = st.sidebar.number_input(
        "Electricity Usage (GJ)",
        value=85.0,
        min_value=0.0,
    )

    heating = st.sidebar.number_input(
        "Heating Usage (GJ)",
        value=45.0,
        min_value=0.0,
    )

    cooling = st.sidebar.number_input(
        "Cooling Usage (GJ)",
        value=50.0,
        min_value=0.0,
    )

    occupancy = st.sidebar.selectbox(
        "Occupancy",
        [
            "Low",
            "Medium",
            "High",
        ],
    )

    indoor_temp = st.sidebar.number_input(
        "Indoor Temperature",
        value=24.0,
    )

    outdoor_temp = st.sidebar.number_input(
        "Outdoor Temperature",
        value=32.0,
    )

    humidity = st.sidebar.slider(
        "Humidity (%)",
        0,
        100,
        55,
    )

    st.sidebar.divider()

    # -----------------------------
    # Optimize Button
    # -----------------------------
    if st.sidebar.button(
        " Optimize Building",
        use_container_width=True,
    ):

        payload = {
            "building_area_m2": building_area,
            "site_energy_gj": site_energy,
            "electricity_gj": electricity,
            "heating_gj": heating,
            "cooling_gj": cooling,
            "occupancy": occupancy,
            "indoor_temperature": indoor_temp,
            "outdoor_temperature": outdoor_temp,
            "humidity": humidity,
        }

        try:

            with st.spinner("🤖 AI is analyzing building..."):

                result = optimize_building(payload)

            st.session_state["optimization_result"] = result
            st.session_state["backend_online"] = True

            st.success(
                f"""
 Analysis Complete!

Priority Area:
**{result.get("priority_area","-")}**

Estimated Savings:
**{result.get("estimated_savings_percent",0)}%**
"""
            )

        except Exception as e:

            st.session_state["backend_online"] = False

            st.error(
                f"Unable to connect to backend.\n\n{e}"
            )

    # -----------------------------
    # Read current result
    # -----------------------------
    result = st.session_state.get(
        "optimization_result"
    )

    # -----------------------------
    # KPI Cards
    # -----------------------------
    st.markdown("##  Performance Metrics")

    render_kpi_cards(result)

    st.divider()

    # -----------------------------
    # Charts
    # -----------------------------
    st.markdown("##  Energy Analytics")

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            build_energy_chart(
                electricity,
                heating,
                cooling,
            ),
            use_container_width=True,
        )

    with col2:

        st.plotly_chart(
            build_savings_chart(result),
            use_container_width=True,
        )

    st.divider()

    # -----------------------------
    # AI Recommendations
    # -----------------------------
    render_recommendation_cards(result)

    st.divider()

    st.caption(
        "EcoLoop Building Agent • Honeywell Hackathon • Powered by FastAPI, EnergyPlus & Groq"
    )


if __name__ == "__main__":
    main()