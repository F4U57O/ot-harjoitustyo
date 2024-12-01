from initialize_database import initialize_database
from database_connection import get_database_connection


def build(test=False):
    connection = get_database_connection(test=test)
    initialize_database(connection)


if __name__ == "__main__":
    build(test=False)
    build(test=True)
