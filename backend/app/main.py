from fastapi import FastAPI

from app.api.v1.endpoints import appointments, auth, face_shape, hair_health, hairstyle
from app.config import settings
from app.middleware.cors import setup_cors
from app.middleware.error_handler import setup_error_handlers
from app.models.schemas import HealthResponse

app = FastAPI(title=settings.app_name, version="1.0.0")
setup_cors(app)
setup_error_handlers(app)


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    return HealthResponse()


app.include_router(face_shape.router, prefix=settings.api_v1_prefix)
app.include_router(hairstyle.router, prefix=settings.api_v1_prefix)
app.include_router(hair_health.router, prefix=settings.api_v1_prefix)
app.include_router(appointments.router, prefix=settings.api_v1_prefix)
app.include_router(auth.router, prefix=settings.api_v1_prefix)
