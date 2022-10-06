import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    #### Créé une connection de la base de donnée vers une base de donnée SQLite
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    create_connection(r"D:\sqlite\db\pythonsqlite.db")
