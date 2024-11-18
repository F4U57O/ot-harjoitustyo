from database_connection import get_database_connection

def drop_tables():
  connection = get_database_connection()
  cursor = connection.cursor()

  cursor.execute('''
      DROP TABLE IF EXISTS users;
  ''')

  connection.commit()
  connection.close()

def create_tables():
  connection = get_database_connection()
  cursor = connection.cursor()

  cursor.execute('''
      CREATE TABLE IF NOT EXISTS users (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE NOT NULL,
          password TEXT NOT NULL
      )
  ''')

  connection.commit()
  connection.close()

def initialize_database():
  connection = get_database_connection()

  drop_tables()
  create_tables()

if __name__ == "__main__":
  initialize_database()