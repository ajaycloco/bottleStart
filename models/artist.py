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

    @classmethod
    def create(cls, data, session):
        columns_keys = cls.__table__.columns.keys()
        columns_keys.remove("id")
        columns_keys.remove("created_at")
        columns_keys.remove("updated_at")
        data_filtered = {key: data[key] for key in columns_keys}
        new_user = cls(**data_filtered)
        session.add(new_user)
        session.commit()

    @classmethod
    def update(cls, data, session, artist):
        columns_keys = cls.__table__.columns.keys()
        columns_keys.remove("id")
        columns_keys.remove("created_at")
        columns_keys.remove("updated_at")
        filtered_data = {key: data[key] for key in columns_keys}
        artist.update(filtered_data)
        session.commit()
