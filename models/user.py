from BaseModel import *
from sqlalchemy import BIGINT, VARCHAR
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.orm import Mapped, MappedColumn
from db.db_connector import engine_info


class User(BaseModel):
    __tablename__ = 'users'
    id: Mapped[int] = MappedColumn(BIGINT, primary_key=True)
    first_name: Mapped[str] = MappedColumn(VARCHAR(255))
    last_name: Mapped[str] = MappedColumn(VARCHAR(255))
    email: Mapped[str] = MappedColumn(VARCHAR(255), unique=True)
    password: Mapped[str] = MappedColumn(VARCHAR(255))
    phone: Mapped[str] = MappedColumn(VARCHAR(20))
    gender: Mapped[str] = MappedColumn(ENUM('M', 'F', 'O'))
    address: Mapped[str] = MappedColumn(VARCHAR(255))


engine = engine_info()

BaseModel.metadata.create_all(engine)
