"""
Modelo Consultation.

Cada registro representa una consulta médica (Primera Vez o Control),
con todas las secciones de la historia clínica física: anamnesis,
antecedentes, lensometría/agudeza visual, queratometría, retinoscopía,
subjetivo, estado motor y cierre (diagnóstico/conducta/observaciones).

La estructura sigue exactamente BASE_DATOS.md, que a su vez replica
los formatos oficiales en la carpeta `formatos/`.

Regla del proyecto: nunca eliminar consultas. Se usa `is_active` para
inactivación lógica si alguna vez se necesita.
"""

import enum
from datetime import date, datetime
from typing import Optional, List

from sqlalchemy import (
    JSON,
    Boolean,
    Date,
    DateTime,
    Enum,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class TipoConsulta(str, enum.Enum):
    primera_vez = "primera_vez"
    control = "control"


class EstadoConsulta(str, enum.Enum):
    en_progreso = "en_progreso"
    finalizada = "finalizada"


class Consultation(Base):
    __tablename__ = "consultations"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)

    patient_id: Mapped[int] = mapped_column(
        ForeignKey("patients.id"), nullable=False
    )

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id"), nullable=False
    )

    tipo_consulta: Mapped[TipoConsulta] = mapped_column(
        Enum(TipoConsulta), nullable=False
    )

    estado: Mapped[EstadoConsulta] = mapped_column(
        Enum(EstadoConsulta),
        default=EstadoConsulta.en_progreso,
        nullable=False,
    )

    fecha_consulta: Mapped[Optional[date]] = mapped_column(
        Date,
        nullable=True
    )


    # --- Anamnesis ---
    anamnesis: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


    # --- Antecedentes ---
    antecedentes_oculares: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    antecedentes_farmacologicos: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    antecedentes_generales: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


    # --- Lensometría y Agudeza Visual ---
    clase_lentes: Mapped[Optional[str]] = mapped_column(String(150), nullable=True)

    vl_od_avsc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vl_od_cc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vl_od_ph: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    vl_oi_avsc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vl_oi_cc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vl_oi_ph: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    vp_od_avsc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vp_od_cc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vp_od_ph: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    vp_oi_avsc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vp_oi_cc: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    vp_oi_ph: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


    # --- Queratometría ---
    queratometria_od: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    queratometria_oi: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)


    # --- Retinoscopía ---
    retinoscopia_od_formula: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    retinoscopia_od_v: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    retinoscopia_oi_formula: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    retinoscopia_oi_v: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    retinoscopia_observaciones: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


    # --- Subjetivo ---
    subjetivo_od_formula: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    subjetivo_od_v: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    subjetivo_od_extra: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    subjetivo_oi_formula: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    subjetivo_oi_v: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    subjetivo_oi_extra: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    adicion_od: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    adicion_oi: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)


    # --- Estado Motor ---
    cover_test_vl: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    cover_test_vp: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    hirschberg: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    angulo_kappa_od: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)
    angulo_kappa_oi: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)

    vision_color: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    estereopsis: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    distancia_pupilar: Mapped[Optional[str]] = mapped_column(String(50), nullable=True)


    # --- Cierre ---
    diagnosticos: Mapped[Optional[list]] = mapped_column(JSON, nullable=True)

    conducta: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    observaciones: Mapped[Optional[str]] = mapped_column(Text, nullable=True)


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


    patient: Mapped["Patient"] = relationship(
        back_populates="consultations"
    )

    user: Mapped["User"] = relationship(
        back_populates="consultations"
    )

    documents: Mapped[List["Document"]] = relationship(
        back_populates="consultation"
    )


    def __repr__(self) -> str:
        return (
            f"<Consultation id={self.id} "
            f"patient_id={self.patient_id} "
            f"tipo={self.tipo_consulta}>"
        )