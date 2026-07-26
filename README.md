# 🏢 EcoLoop Building Agent

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-LLM-black?style=for-the-badge)
![EnergyPlus](https://img.shields.io/badge/EnergyPlus-Simulation-blue?style=for-the-badge)
![AWS EC2](https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazonaws&logoColor=white)
![License](https://img.shields.io/badge/License-Hackathon-green?style=for-the-badge)

</p>

---

# 📖 Overview

EcoLoop Building Agent is an AI-powered Building Energy Optimization Platform designed to help facility managers and building operators reduce energy consumption, operational costs, and carbon emissions through intelligent data-driven recommendations.

The platform combines **EnergyPlus building simulation**, **FastAPI**, **Groq Llama-3.3-70B**, and **Streamlit** to transform raw building performance metrics into actionable optimization insights. By analyzing key parameters such as electricity usage, HVAC consumption, occupancy, indoor and outdoor environmental conditions, the system identifies inefficiencies and generates personalized recommendations for improving overall building performance.

Unlike conventional monitoring dashboards that only visualize energy usage, EcoLoop Building Agent leverages Large Language Models (LLMs) to perform contextual reasoning over building data, estimate potential energy savings, identify high-impact optimization areas, and recommend practical strategies that support sustainable and energy-efficient building management.

The solution delivers an intuitive web dashboard with interactive analytics, AI-generated recommendations, estimated cost savings, CO₂ reduction metrics, and confidence scores, enabling users to make informed operational decisions in real time.

---

# ✨ Key Features

-  **AI-Powered Energy Optimization** using Groq Llama-3.3-70B to generate intelligent, context-aware building optimization strategies.

-  **EnergyPlus Simulation Analysis** for processing building energy simulation outputs and extracting meaningful performance indicators.

-  **Real-Time Optimization Engine** that evaluates building metrics and predicts high-impact energy improvement opportunities.

-  **Interactive Analytics Dashboard** built with Streamlit featuring KPI cards, visual charts, and intuitive user interaction.

-  **Comprehensive Energy Insights** including electricity, heating, cooling, occupancy, and environmental performance analysis.

-  **Sustainability Assessment** through estimated CO₂ emission reduction and energy efficiency scoring.

-  **Estimated Energy Savings** with AI-driven prediction of potential operational cost reductions.

-  **Priority-Based Recommendations** ranked according to expected impact and optimization potential.

-  **RESTful FastAPI Backend** enabling scalable communication between the frontend and AI optimization services.

-  **Cloud Deployment on AWS EC2** providing secure and scalable backend hosting with public API access.

-  **LLM-Driven Decision Support** that converts structured building metrics into human-readable optimization recommendations.

-  **Modular Architecture** separating presentation, API, optimization engine, and AI inference layers for maintainability and scalability.

-  **Responsive User Interface** designed for facility managers, energy auditors, and building operators.

-  **Extensible Design** allowing future integration with IoT sensors, Building Management Systems (BMS), Digital Twins, and predictive maintenance solutions.


---

# 🏗️ System Architecture

<img width="1366" height="1034" alt="image" src="https://github.com/user-attachments/assets/3aaef976-9878-4655-ad7d-5dc1fd6a1479" />


<p align="center">

<img src="docs/architecture.png" width="900">

</p>

---

# 🔄 Optimization Workflow

<p align="center">

<img src="docs/workflow.png" width="900">

</p>

The optimization workflow consists of:

1. User enters building parameters.
2. Streamlit validates the inputs.
3. FastAPI receives the optimization request.
4. Building metrics are processed.
5. Prompt is generated.
6. Groq LLM performs AI inference.
7. Recommendations are generated.
8. Results are returned as JSON.
9. Dashboard visualizes KPIs and charts.

---
<img width="896" height="1048" alt="image" src="https://github.com/user-attachments/assets/c9089c27-c90b-443d-996c-c9ab2192a2ec" />


# 🧠 AI Recommendation Pipeline

<p align="center">

<img src="docs/ai_pipeline.png" width="900">

</p>

The AI pipeline includes:

- EnergyPlus Report Parsing
- Feature Extraction
- Prompt Engineering
- Groq LLM Inference
- Optimization Engine
- Recommendation Generator
- Dashboard Visualization

---

<img width="932" height="500" alt="image" src="https://github.com/user-attachments/assets/edf514d6-619a-4640-9fa4-701065bd39b2" />


# ☁️ AWS Deployment Architecture

<p align="center">

<img src="docs/aws_architecture.png" width="900">

</p>

Deployment Stack

```
Internet User
        │
        ▼
Streamlit Community Cloud
        │
 HTTPS REST API
        │
        ▼
AWS EC2 Instance
        │
──────────────────────────────
Python Virtual Environment
        │
Uvicorn Server
        │
FastAPI Application
        │
Optimization Engine
        │
Groq API
──────────────────────────────
```

---

<img width="940" height="470" alt="image" src="https://github.com/user-attachments/assets/c15b5b75-710e-411c-9543-f963c5bbca81" />


# ⚙️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Frontend | Streamlit, Plotly |
| Backend | FastAPI, Uvicorn |
| AI | Groq Llama-3.3-70B |
| Simulation | EnergyPlus |
| Parsing | BeautifulSoup |
| Visualization | Plotly |
| Cloud | AWS EC2 |
| Version Control | GitHub |

---

# 📁 Project Structure

```text
EcoLoop-Building-Agent
│
├── app
│   ├── agents
│   ├── api
│   ├── config
│   ├── models
│   ├── services
│   ├── utils
│   └── main.py
│
├── data
├── reports
├── styles
├── tests
│
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .env
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/iramk596/EcoLoop-Building-Agent.git
```

```bash
cd EcoLoop-Building-Agent
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
venv\Scripts\activate
```

Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a `.env` file

```env
GROQ_API_KEY=your_groq_api_key
```

---

# ▶️ Run Backend

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Swagger Documentation

```
http://localhost:8000/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run streamlit_app.py
```

---

# 📡 REST API

## POST /optimize

Request

```json
{
  "building_area":1200,
  "site_energy":180,
  "electricity_usage":85,
  "heating_usage":45,
  "cooling_usage":50,
  "occupancy":"Low",
  "indoor_temperature":24,
  "outdoor_temperature":32,
  "humidity":55
}
```

Response

```json
{
  "energy_efficiency_score":86,
  "estimated_savings_percent":22,
  "estimated_co2_reduction_percent":18,
  "confidence_score":92,
  "priority_area":"HVAC",
  "recommendations":[]
}
```

---

# 📊 Dashboard

The Streamlit dashboard provides

- Energy Efficiency Score
- Estimated Savings
- CO₂ Reduction
- Confidence Score
- Interactive Charts
- Building Analytics
- AI Recommendations

---

# 📸 Screenshots

## Dashboard

<img width="2553" height="1356" alt="image" src="https://github.com/user-attachments/assets/01a4e3ce-781f-4b3d-a7d9-f44489514be3" />


---

## Analytics

<img src="docs/analytics.png" width="900">

---

## AI Recommendations

<img src="docs/recommendations.png" width="900">

---

# 🌟 Future Scope

- IoT Sensor Integration
- Real-time Monitoring
- Predictive Maintenance
- HVAC Automation
- Renewable Energy Optimization
- Multi-building Management
- Digital Twin Integration
- Carbon Footprint Analytics

---

# 👨‍💻 Team

Developed for the **Honeywell Hackathon**.

---

# 📜 License

This project is intended for educational and hackathon purposes only.

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

```
⭐ Star this repository if you like the project!
```
