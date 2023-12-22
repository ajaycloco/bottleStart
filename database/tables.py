from db_connector import *
connection = connect_to_db()

if connection.is_connected():
    print("Running Migrations.......")
else:
    print("Database Connection Failed")
    exit()

cursor = connection.cursor()

tables = list()

# create users table
users_table = """
            CREATE TABLE IF NOT EXISTS users(
            id INTEGER AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            email VARCHAR(255),
            password VARCHAR(500),
            phone VARCHAR(20),
            gender ENUM('M','F','O'),
            address VARCHAR(255),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            )
            """
tables.append(users_table)


# create artist table
artist_table = """
              CREATE TABLE IF NOT EXISTS artist(
              id INTEGER AUTO_INCREMENT PRIMARY KEY,
              name VARCHAR(255),
              gender ENUM('M','F','O'),
              address VARCHAR(255),
              first_release_year TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              no_of_albums_released INTEGER DEFAULT 0,
              created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
              updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
              )
              """
tables.append(artist_table)


# music table
music_table = """
            CREATE TABLE IF NOT EXISTS music(
            artist_id INTEGER,
            title VARCHAR(255),
            album_name VARCHAR(255),
            genre ENUM('rnb','country','classic','rock','jazz'),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY(artist_id) REFERENCES artist(id)
            )
            """
tables.append(music_table)

for table in tables:
    cursor.execute(table)

# Commit the changes to the database
connection.commit()

cursor.close()

# Close the database connection
connection.close()

print("Completed Migrations")
exit()
