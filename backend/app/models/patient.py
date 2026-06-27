"""
Modelo Patient.

Contiene la información administrativa permanente del paciente.
Estos datos NO pertenecen a una consulta específica (ver BASE_DATOS.md).

Regla del proyecto: nunca eliminar pacientes físicamente.
Por eso se incluye `is_active` para inactivación lógica en lugar de DELETE.
"""

from datetime import date, datetime
from typing import Optional, List

from sqlalchemy import Boolean, Date, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    nombre_completo: Mapped[str] = mapped_column(
        String(200),
        nullable=False
    )

    tipo_documento: Mapped[Optional[str]] = mapped_column(
        String(20),
        nullable=True
    )

    documento: Mapped[Optional[str]] = mapped_column(
        String(50),
        index=True,
        nullable=True
    )


    fecha_nacimiento: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True
    )

    edad: Mapped[Optional[int]] = mapped_column(
        nullable=True
    )

    sexo: Mapped[Optional[str]] = mapped_column(
        String(20),
        nullable=True
    )

    estado_civil: Mapped[Optional[str]] = mapped_column(
        String(30),
        nullable=True
    )


    direccion: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )

    ciudad: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    telefono: Mapped[Optional[str]] = mapped_column(
        String(30),
        nullable=True
    )

    correo: Mapped[Optional[str]] = mapped_column(
        String(150),
        nullable=True
    )


    eps: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    entidad: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )

    numero_carnet: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True
    )

    ocupacion: Mapped[Optional[str]] = mapped_column(
        String(100),
        nullable=True
    )


    remitido_por: Mapped[Optional[str]] = mapped_column(
        String(150),
        nullable=True
    )

    acompanante: Mapped[Optional[str]] = mapped_column(
        String(150),
        nullable=True
    )

    telefono_acompanante: Mapped[Optional[str]] = mapped_column(
        String(30),
        nullable=True
    )

    origen_enfermedad: Mapped[Optional[str]] = mapped_column(
        String(255),
        nullable=True
    )


    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )


    consultations: Mapped[List["Consultation"]] = relationship(
        back_populates="patient"
    )


    def __repr__(self) -> str:
        return f"<Patient id={self.id} nombre={self.nombre_completo!r}>"