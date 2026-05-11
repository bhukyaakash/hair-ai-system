import base64


def decode_base64_image(image_base64: str) -> bytes:
    return base64.b64decode(image_base64)
