"""
Punto de entrada de la API.

En esta fase solo se configura:
- La aplicación FastAPI.
- CORS para permitir la conexión con el frontend (Next.js).
- Un endpoint de salud ("/" y "/health") para verificar que el backend
  está corriendo y conectado a la base de datos.

Los CRUD (Pacientes, Consultas, Documentos) y la autenticación se
implementarán en las siguientes fases, según GUIA_DESARROLLO.md.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text

from app.core.config import settings
from app.db.base import Base
from app.db.session import engine

# Importar los modelos para que queden registrados en Base.metadata
import app.models  # noqa: F401

app = FastAPI(
    title="Optometría API",
    description="API del sistema de historia clínica para optometría.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    """
    Crea las tablas si no existen.

    Nota: para el desarrollo normal de los modelos se utilizan migraciones
    con Alembic (ver carpeta `alembic/`). Esta creación automática es solo
    una red de seguridad para entornos locales nuevos.
    """
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root() -> dict[str, str]:
    return {"mensaje": "API de Optometría funcionando correctamente."}


@app.get("/health")
def health_check() -> dict[str, str]:
    """Verifica que la API esté corriendo y que la base de datos responda."""
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        db_status = "conectada"
    except Exception:
        db_status = "error"

    return {"api": "ok", "base_de_datos": db_status}
