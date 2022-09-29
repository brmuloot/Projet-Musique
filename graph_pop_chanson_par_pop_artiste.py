import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def create_top(conn,top):

    sql = ''' INSERT INTO top(id,followers,genres,name,popularity)
              VALUES(?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, top)
    conn.commit()



import matplotlib.pyplot as plt
def main():
    database = r"D:\ressources\sources_data.db"

    # create a database connection
    conn = create_connection(database)
    with conn:
           # create a new project
        cur = conn.cursor()
        cur.execute("SELECT * FROM artistes ORDER BY popularity DESC limit 10000")
        rows=cur.fetchall()
        
        cur.execute("SELECT * FROM chansons ORDER BY popularity DESC limit 10000")
        rows2=cur.fetchall()
        
        # for row  in rows:
        #     print(row)
        #     print("\n")

        popularity_chansons = []
        popularity_artistes = []

        for row in rows:
            popularity_artistes.append(row[4])

        for row in rows2:
            popularity_chansons.append(row[2])


        plt.scatter(popularity_chansons, popularity_artistes)
        plt.xlabel("popularité chansons")
        plt.ylabel("popularité artistes")
        plt.show()


        
        # compteur = 0
        # test = []
        # for row in rows:
        #     x=rows[compteur]
            
        #     test.append(x)
        #     compteur += 1
        # print(test)

        





if __name__ == '__main__':
    main()

#### A ENTRER DANS LE TERMINAL :
# sqlite3 d:\sqlite\db\pythonsqlite.db
# .header on
# .mode column
# SELECT * FROM projects;