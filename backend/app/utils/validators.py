"""Data Validators"""

from fastapi import UploadFile
from ..config import settings


def validate_image_file(file: UploadFile) -> bool:
    """
    Validate if uploaded file is a valid image
    """
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        return False
    return True


def validate_file_size(file: UploadFile) -> bool:
    """
    Validate file size
    """
    if file.size and file.size > settings.MAX_IMAGE_SIZE:
        return False
    return True


def validate_email(email: str) -> bool:
    """
    Validate email format
    """
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None
