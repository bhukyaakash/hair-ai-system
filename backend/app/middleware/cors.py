"""CORS Configuration"""

from fastapi.middleware.cors import CORSMiddleware


def setup_cors(app, settings):
    """
    Setup CORS middleware
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
