

def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('DROP TABLE IF EXISTS users;')
    cursor.execute('DROP TABLE IF EXISTS workouts;')
    cursor.execute('DROP TABLE IF EXISTS game_stats;')
    cursor.execute('DROP TABLE IF EXISTS goals')

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

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS goals (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   goal TEXT NOT NULL,
                   status TEXT CHECK(status IN ('käynnissä', 'suoritettu', 'ei suoritettu')) NOT NULL DEFAULT 'in progress',
                   created_at TEXT,
                   status_updated_at TEXT,
                   FOREIGN KEY (user_id) REFERENCES users (id)
            )
            ''')

    connection.commit()


def initialize_database(connection):
    drop_tables(connection)
    create_tables(connection)
