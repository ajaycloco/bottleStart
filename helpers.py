from sqlalchemy.orm import class_mapper
from sqlalchemy.orm.attributes import InstrumentedAttribute
from datetime import datetime

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def orm_to_json(model):
    column_keys = model.__table__.columns.keys()

    artist_data = {col_key: getattr(model, col_key) for col_key in column_keys}

    artist_data.pop('_sa_instance_state', None)

    for date_key in ['created_at', 'updated_at', 'dob', 'first_release_year']:
        if artist_data.get(date_key):
            artist_data[date_key] = artist_data[date_key].strftime(DATE_FORMAT)

    return artist_data
