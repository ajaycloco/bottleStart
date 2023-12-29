from .base import BaseModel
from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy import BIGINT, VARCHAR
from sqlalchemy.schema import ForeignKey


class Token(BaseModel):
    __tablename__ = 'tokens'
    id: Mapped[int] = MappedColumn(BIGINT, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = MappedColumn(BIGINT, ForeignKey('users.id'), nullable=False)
    access_token: Mapped[str] = MappedColumn(VARCHAR(1000), nullable=False)
    refresh_token: Mapped[str] = MappedColumn(VARCHAR(1000), nullable=True)
