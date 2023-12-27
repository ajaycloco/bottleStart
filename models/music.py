from .base import BaseModel
from sqlalchemy import INTEGER, DATETIME, BIGINT, VARCHAR, Enum
from sqlalchemy.orm import Mapped, MappedColumn
from sqlalchemy.dialects.mysql import ENUM
from sqlalchemy.schema import ForeignKey

class Music(BaseModel):
    __tablename__ = "musics"
    id: Mapped[int] = MappedColumn(BIGINT, primary_key=True, autoincrement=True)
    artist_id: Mapped[int] = MappedColumn(ForeignKey('artists.id'), nullable=False)
    title: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False)
    album_name: Mapped[str] = MappedColumn(VARCHAR(255))
    genre: Mapped[str] = MappedColumn(ENUM('rnb', 'country', 'classic', 'rock', 'jazz'),nullable=False)

