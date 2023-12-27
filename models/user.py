import datetime

from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy import BIGINT, VARCHAR, BOOLEAN, DATETIME, func
from .base import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = MappedColumn(BIGINT, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False)
    email: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False, unique=True)
    password: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False)
    status: Mapped[bool] = MappedColumn(BOOLEAN, default=False)


