import datetime

from sqlalchemy.orm import MappedColumn, Mapped
from sqlalchemy import BIGINT, VARCHAR, BOOLEAN, DATETIME, func
from base import BaseModel
from db_engine import sql_engine


class User(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = MappedColumn(BIGINT, primary_key=True, autoincrement=True)
    full_name: Mapped[str] = MappedColumn(VARCHAR(255))
    email: Mapped[str] = MappedColumn(VARCHAR(255), unique=True)
    password: Mapped[str] = MappedColumn(VARCHAR(255))
    status: Mapped[bool] = MappedColumn(BOOLEAN, default=False)


engine = sql_engine()
BaseModel.metadata.create_all(engine)
