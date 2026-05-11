class AppointmentService:
    @staticmethod
    def create_appointment(name: str, email: str, datetime_iso: str) -> dict:
        return {"name": name, "email": email, "scheduled_at": datetime_iso, "status": "booked"}
