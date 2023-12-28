from sqlalchemy import URL, create_engine
from sqlalchemy.orm import sessionmaker
from environs import Env


def sql_engine():
    env = Env()
    env.read_env()
    url = URL.create(
        drivername='mysql+mysqlconnector',
        host=env.str("db_host"),
        port=env.str("db_port"),
        database=env.str("db_name"),
        username=env.str("db_user"),
        password=env.str("db_password")
    )
    engine = create_engine(url, echo=True)
    # return engine
    session_pool = sessionmaker(engine)
    # return session_pool()
    with session_pool() as session:
        return session
