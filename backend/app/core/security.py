"""
Utilidades de seguridad.

Contiene:
- Hash y verificación de contraseñas (bcrypt).
- Creación y decodificación de tokens JWT.

No implementa endpoints todavía; eso corresponde a la fase de autenticación
descrita en GUIA_DESARROLLO.md.
"""

from datetime import datetime, timedelta, timezone
from typing import Any

import bcrypt
from jose import JWTError, jwt

from app.core.config import settings


def hash_password(plain_password: str) -> str:
    """Genera el hash bcrypt de una contraseña en texto plano."""
    password_bytes = plain_password.encode("utf-8")
    hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password: str, password_hash: str) -> bool:
    """Verifica una contraseña en texto plano contra su hash bcrypt."""
    return bcrypt.checkpw(
        plain_password.encode("utf-8"), password_hash.encode("utf-8")
    )


def create_access_token(data: dict[str, Any]) -> str:
    """Crea un token JWT firmado con expiración configurable."""
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


def decode_access_token(token: str) -> dict[str, Any] | None:
    """Decodifica un token JWT. Retorna None si es inválido o expiró."""
    try:
        return jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
    except JWTError:
        return None
