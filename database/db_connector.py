# db connection and connection session pool using sql alchemy
from sqlalchemy import create_engine, URL, text
from sqlalchemy.orm import sessionmaker


url = URL.create(
    drivername='mysql+mysqlconnector',
    host='localhost',
    port=3306,
    database='artist_management',
    username='root',
    password='test'
)

engine = create_engine(url, echo=True)
session_pool = sessionmaker(bind=engine)
with session_pool() as session:
    session.execute(text('SHOW tables;'))
    session.commit()
    session.rollback()


# core db setup for python
# import mysql.connector
#
#
# def connect_to_db():
#     host = ''
#     user = 'root'
#     password = 'test'
#     database = 'artist_management'
#
#     connection = mysql.connector.connect(
#         host=host,
#         user=user,
#         password=password,
#         database=database
#     )
#     return connection
#
