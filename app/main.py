from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="EcoLoop Building Agent API",
    description="AI-powered Building Energy Optimization System",
    version="1.0.0",
)

app.include_router(router)