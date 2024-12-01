from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS users;')
    cursor.execute('DROP TABLE IF EXISTS workouts;')
    cursor.execute('DROP TABLE IF EXISTS game_stats;')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE NOT NULL,
          password TEXT NOT NULL
      )
  ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            date TEXT NOT NULL,
            activity TEXT NOT NULL,
            duration TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS game_stats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            opponent TEXT NOT NULL,
            date TEXT NOT NULL,
            goals INTEGER,
            assists INTEGER,
            play_time INTEGER,
            rating INTEGER,
            feedback TEXT NOT NULL,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
    ''')

    connection.commit()


def initialize_database(connection):
    drop_tables(connection)
    create_tables(connection)