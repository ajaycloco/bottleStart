import mysql.connector


def connect_to_db():
    host = ''
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

