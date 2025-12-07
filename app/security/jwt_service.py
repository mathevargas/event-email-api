import os
import jwt
from fastapi import HTTPException, status
from dotenv import load_dotenv

load_dotenv()

SECRET = os.getenv("JWT_SECRET")

if not SECRET:
    raise Exception("JWT_SECRET não configurado no .env")

class JwtService:

    @staticmethod
    def validar_token(token: str):
        try:
            payload = jwt.decode(token, SECRET, algorithms=["HS256"])
            return payload.get("sub")  # email do usuário
        except Exception:
            return None
