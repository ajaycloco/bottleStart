from datetime import datetime
from sqlalchemy import DATETIME, func
from sqlalchemy.orm import DeclarativeBase, Mapped, MappedColumn


class BaseModel(DeclarativeBase):
    created_at: Mapped[datetime] = MappedColumn(DATETIME, default=func.now())
    updated_at: Mapped[datetime] = MappedColumn(DATETIME, default=func.now(), onupdate=func.now())

