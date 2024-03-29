import ssl
from typing import Generator
from fastapi import HTTPException, Request, status
import jwt
from pydantic import ValidationError
from app.config import settings


from app.db.session import SessionLocal


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def deny():
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized",
    )


def extract_token_from_header(header: str):
    parts = header.split(" ")
    return parts[1] if len(parts) == 2 and parts[0].lower() == "bearer" else None


def get_current_user(request: Request) -> str:
    authorization = request.headers.get("authorization")

    if not (authorization):
        return deny()

    token = extract_token_from_header(authorization)

    if not token:
        return deny()
    try:
        ssl_context = ssl.create_default_context()
        ssl_context.check_hostname = False
        ssl_context.verify_mode = ssl.CERT_NONE

        jwks_client = jwt.PyJWKClient(
            settings.HANKO_API_URL + "/.well-known/jwks.json", ssl_context=ssl_context
        )
        signing_key = jwks_client.get_signing_key_from_jwt(token)

        data = jwt.decode(
            token,
            signing_key.key,
            algorithms=[settings.ALGORITHM],
            audience="localhost",  # str(settings.SERVER_HOST),
        )
    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials",
        )
    user = data.get("sub")

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
