from sqlalchemy import URL, create_engine


def sql_engine():
    url = URL.create(
        drivername='mysql+mysqlconnector',
        host='localhost',
        port=3306,
        database='artist_management',
        username='root',
        password='test'
    )
    engine = create_engine(url, echo=True)
    return engine
