from enum import Enum


class FaceShape(str, Enum):
    oval = "oval"
    round = "round"
    square = "square"
    heart = "heart"
    diamond = "diamond"


class HairHealthStatus(str, Enum):
    healthy = "healthy"
    moderate = "moderate"
    critical = "critical"
