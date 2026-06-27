"""
Modelo Document.

Cada documento generado (historia clínica, certificado, orden, remisión
o fórmula) queda registrado, según BASE_DATOS.md y DECISIÓN 013-015.
"""

import enum
from datetime import datetime
from typing import Optional

from sqlalchemy import Boolean, DateTime, Enum, ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TipoDocumento(str, enum.Enum):
    historia_clinica = "historia_clinica"
    certificado = "certificado"
    orden = "orden"
    remision = "remision"
    formula = "formula"


class Document(Base):
    __tablename__ = "documents"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    consultation_id: Mapped[int] = mapped_column(
        ForeignKey("consultations.id"),
        nullable=False
    )

    tipo: Mapped[TipoDocumento] = mapped_column(
        Enum(TipoDocumento),
        nullable=False
    )

    texto_personalizado: Mapped[Optional[str]] = mapped_column(
        Text,
        nullable=True
    )

    incluir_encabezado: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    incluir_firma: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    pdf_path: Mapped[Optional[str]] = mapped_column(
        String(500),
        nullable=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    consultation: Mapped["Consultation"] = relationship(
        back_populates="documents"
    )

    def __repr__(self) -> str:
        return f"<Document id={self.id} tipo={self.tipo}>"