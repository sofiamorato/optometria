"""
Exporta todos los modelos para que Alembic y SQLAlchemy los detecten
fácilmente al importar `app.models`.
"""

from app.models.consultation import Consultation, EstadoConsulta, TipoConsulta
from app.models.document import Document, TipoDocumento
from app.models.patient import Patient
from app.models.user import User

__all__ = [
    "User",
    "Patient",
    "Consultation",
    "TipoConsulta",
    "EstadoConsulta",
    "Document",
    "TipoDocumento",
]
