"""
Modelo User.

En el MVP solo existirá una doctora, pero el modelo queda preparado
para soportar múltiples usuarios en el futuro (ver DECISIÓN 002).
"""

from datetime import datetime
from typing import Optional, List

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True
    )

    nombre: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )


    titulo_profesional: Mapped[Optional[str]] = mapped_column(
        String(150),
        nullable=True
    )

    registro_medico: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True
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
        back_populates="user"
    )


    def __repr__(self) -> str:
        return f"<User id={self.id} email={self.email!r}>"