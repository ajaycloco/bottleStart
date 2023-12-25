from sqlalchemy.ext.declarative import declared_attr


class TableNameMixin:
    @declared_attr
    def __table_name__(cls) -> str:
        return cls.__name__.lower() + "s"

