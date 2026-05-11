class FaceShapeClassifier:
    def predict(self, _: bytes) -> tuple[str, float]:
        return "oval", 0.9
