from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def setup_error_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def generic_exception_handler(_: Request, exc: Exception):
        return JSONResponse(status_code=500, content={"detail": str(exc)})
