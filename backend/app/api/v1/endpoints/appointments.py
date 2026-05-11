from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

from app.services.appointment_service import AppointmentService

router = APIRouter(prefix="/appointments", tags=["appointments"])


class AppointmentRequest(BaseModel):
    name: str
    email: EmailStr
    scheduled_at: str


@router.post("/")
async def book_appointment(payload: AppointmentRequest):
    return AppointmentService.create_appointment(payload.name, payload.email, payload.scheduled_at)
