from app.models.enums import FaceShape


class HairstyleService:
    @staticmethod
    def recommend(face_shape: FaceShape) -> list[str]:
        mapping = {
            FaceShape.oval: ["Layered Bob", "Pompadour", "Textured Crop"],
            FaceShape.round: ["Long Layers", "Angular Bob", "Quiff"],
            FaceShape.square: ["Soft Waves", "Side Part", "Fringe"],
            FaceShape.heart: ["Chin-Length Bob", "Side-Swept Bangs", "Wavy Lob"],
            FaceShape.diamond: ["Curtain Bangs", "Volume Top", "Shoulder Waves"],
        }
        return mapping.get(face_shape, ["Classic Cut"])
