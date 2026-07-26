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

EcoLoop Building Agent is an AI-powered building energy optimization platform that combines **EnergyPlus building simulation**, **FastAPI**, **Groq LLM**, and **Streamlit** to provide intelligent recommendations for improving building energy efficiency.

The platform analyzes building performance metrics, predicts optimization opportunities, estimates energy savings and CO₂ reduction, and generates actionable recommendations using Large Language Models (LLMs).

---

# ✨ Key Features

- 🤖 AI-powered building energy optimization
- ⚡ Groq Llama-3.3-70B integration
- 🏢 EnergyPlus simulation analysis
- 📊 Interactive Streamlit dashboard
- 🚀 FastAPI REST backend
- 📈 Energy analytics and visualization
- 🌱 CO₂ reduction estimation
- 💰 Estimated energy savings
- 📋 Priority-based recommendations
- ☁️ AWS EC2 deployment
- 📱 Responsive dashboard

---

# 🏗️ System Architecture

> Replace this image with your final architecture diagram.

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

<img src="docs/dashboard.png" width="900">

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
