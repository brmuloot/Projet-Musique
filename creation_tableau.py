import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    #### Créé une connection de la base de donnée vers une base de donnée SQLite
    #### spécifié par un fichier .db 
    #### :paramètre db_file: fichier .db
    #### :return: Connection à l'objet ou non

    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    #### Création d'une table à partir d l'instruction create_table_sql
    #### :paramètre com: Connection à l'objet
    #### :paramètre create_table_sql: une instruction de création de table (CREATE TABLE)
    #### :return:

    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"D:\sqlite\db\pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS projects (
                                        id integer PRIMARY KEY,
                                        name text NOT NULL,
                                        begin_date text,
                                        end_date text
                                    ); """

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                    id integer PRIMARY KEY,
                                    name text NOT NULL,
                                    priority integer,
                                    status_id integer NOT NULL,
                                    project_id integer NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text NOT NULL,
                                    FOREIGN KEY (project_id) REFERENCES projects (id)
                                );"""

    # création d'une connection à la base de donnée
    conn = create_connection(database)

    # création de la table
    if conn is not None:
        # create projects table
        create_table(conn, sql_create_projects_table)

        # create tasks table
        create_table(conn, sql_create_tasks_table)
    else:
        print("Error! cannot create the database connection.")


if __name__ == '__main__':
    main()

#### ENTRER DANS LA COMMANDE :
#sqlite3 d:\sqlite\db\pythonsqlite.db
#.tables
