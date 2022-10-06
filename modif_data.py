import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn

def update_task(conn, task):
    #### mettre à jour la priorité, la date_debut et la date de fin d'une tâche
    #### :param conn:
    #### :param task:
    #### :return: l'id du projet
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    sql = ''' UPDATE tasks
              SET priority = ? ,
                  begin_date = ? ,
                  end_date = ?
              WHERE id = ?'''
    cur = conn.cursor()
    cur.execute(sql, task)
    conn.commit()

    
def main():
    database = r"D:\sqlite\db\pythonsqlite.db"

    conn = create_connection(database)
    with conn:
        update_task(conn, (2, '2015-01-04', '2015-01-06', 2))


if __name__ == '__main__':
    main()

# A ENTRER DANS LE TERMINAL
# sqlite3 D:\sqlite\db\pythonsqlite.db
# .header on
# .mode column
# SELECT * FROM tasks WHERE id = 2;
