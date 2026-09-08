from fastapi import FastAPI
from app.api.v1.router import router as analytics_router

app = FastAPI(
    title="Pandas Data Analytics API",
    version="1.0.0",
    description="FastAPI service for dataset upload, summary metrics, and analytics",
)


@app.get("/")
def health_check():
    return {"status": "healthy", "service": "pandas-analytics"}


# Register modular v1 analytics router
app.include_router(analytics_router, prefix="/api/v1")