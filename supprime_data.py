import sqlite3
from sqlite3 import Error


def create_connection(db_file):

    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def delete_task(conn, id):
    #### Supprime une tâche par task id
    #### :param conn: Connection à la base de donnée SQLite
    #### :param id: l'id de task
    #### :return:

    sql = 'DELETE FROM tasks WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()


def delete_all_tasks(conn):
    #### Supprime toute les lignes de la table tasks
    #### :param conn:
    #### :return:

    sql = 'DELETE FROM tasks'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()


def main():
    database = r"D:\sqlite\db\pythonsqlite.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
        delete_task(conn, 2);
        # delete_all_tasks(conn);


if __name__ == '__main__':
    main()

# A ENTRER DANS LE TERMINAL
# sqlite3 D:\sqlite\db\pythonsqlite.db
# .header on
# .mode column
# SELECT * FROM tasks;
