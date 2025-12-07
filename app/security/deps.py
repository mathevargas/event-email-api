from fastapi import Header, HTTPException, status
from app.security.jwt_service import JwtService

async def auth_required(authorization: str = Header(None)):

    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token ausente ou inválido"
        )

    token = authorization.split(" ")[1]
    email = JwtService.validar_token(token)

    if not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado"
        )

    return email
