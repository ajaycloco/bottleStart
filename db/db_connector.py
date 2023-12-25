from sqlalchemy import create_engine, URL, text
import mysql.connector


def engine_info():
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


def connect_to_db():
    host = '127.0.0.1'
    user = 'root'
    password = 'test'
    database = 'artist_management'

    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    return connection
