from app.utils.constants import SUPPORTED_IMAGE_TYPES


def validate_content_type(content_type: str) -> bool:
    return content_type in SUPPORTED_IMAGE_TYPES
