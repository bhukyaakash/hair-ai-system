from app.models.enums import HairHealthStatus


class HairHealthService:
    @staticmethod
    def assess(_: str) -> tuple[HairHealthStatus, float, list[str]]:
        return HairHealthStatus.moderate, 0.72, ["Use mild shampoo", "Hydrate scalp"]
