from app.models.enums import FaceShape


class FaceShapeService:
    @staticmethod
    def detect_face_shape(_: str) -> tuple[FaceShape, float]:
        return FaceShape.oval, 0.9
