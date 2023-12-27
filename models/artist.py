from datetime import datetime

from sqlalchemy import INTEGER, VARCHAR, DATETIME, func, BIGINT
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped, MappedColumn
from .base import BaseModel
from db_engine import sql_engine


class Artist(BaseModel):
    __tablename__ = "artists"
    id: Mapped[int] = MappedColumn(BIGINT, primary_key=True, autoincrement=True)
    name: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False)
    dob: Mapped[datetime] = MappedColumn(DATETIME, nullable=False)
    address: Mapped[str] = MappedColumn(VARCHAR(255))
    gender: Mapped[str] = MappedColumn(ENUM("M", "F", "O"), nullable=False)
    first_release_year: Mapped[datetime] = MappedColumn(DATETIME, nullable=False)
    no_of_albums_released: Mapped[int] = MappedColumn(INTEGER, default=0)
