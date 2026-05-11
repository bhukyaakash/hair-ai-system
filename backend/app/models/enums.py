"""Enum Definitions"""

from enum import Enum


class FaceShapeEnum(str, Enum):
    """Face shape types"""
    ROUND = "round"
    OVAL = "oval"
    SQUARE = "square"
    HEART = "heart"
    OBLONG = "oblong"
    DIAMOND = "diamond"


class HairstyleCategoryEnum(str, Enum):
    """Hairstyle categories"""
    MODERN = "modern"
    FUTURISTIC = "futuristic"
    OLD = "old"
    PRESENT = "present"
    OLD_AGE = "old_age"


class HairThicknessEnum(str, Enum):
    """Hair thickness types"""
    THIN = "thin"
    NORMAL = "normal"
    THICK = "thick"


class HairConditionEnum(str, Enum):
    """Hair condition types"""
    DRY = "dry"
    NORMAL = "normal"
    OILY = "oily"


class SeverityEnum(str, Enum):
    """Issue severity"""
    MILD = "mild"
    MODERATE = "moderate"
    SEVERE = "severe"


class AppointmentStatusEnum(str, Enum):
    """Appointment status"""
    SCHEDULED = "scheduled"
    COMPLETED = "completed"
    CANCELLED = "cancelled"
    RESCHEDULED = "rescheduled"
    NO_SHOW = "no_show"
