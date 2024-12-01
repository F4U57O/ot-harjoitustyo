import sqlite3
from config import DATABASE_FILE_PATH, TEST_DATABASE_FILE_PATH


def get_database_connection(test=False):
    database_file = TEST_DATABASE_FILE_PATH if test else DATABASE_FILE_PATH
    connection = sqlite3.connect(database_file)
    connection.row_factory = sqlite3.Row
    return connection
