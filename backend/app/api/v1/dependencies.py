"""Shared API Dependencies"""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthCredentials
import jwt
from ..config import settings

security = HTTPBearer()


async def verify_token(credentials: HTTPAuthCredentials = Depends(security)):
    """
    Verify JWT token from request headers
    """
    token = credentials.credentials
    try:
        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM]
        )
        user_id: str = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        return user_id
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )


async def get_current_user(user_id: str = Depends(verify_token)):
    """
    Get current user from token
    """
    # TODO: Fetch user from database
    return {"user_id": user_id}
