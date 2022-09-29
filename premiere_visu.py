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
        res = cur.execute("SELECT * FROM artistes ORDER BY popularity DESC limit 10000")
        rows=cur.fetchmany(10000)
        
        # for row  in rows:
        #     print(row)
        #     print("\n")


        follower = []
        popularity = []
        for row in rows:
            follower.append(row[1])
            popularity.append(row[4])
        print(follower)
        print(popularity)
        plt.scatter(follower, popularity)
        plt.xlabel("nombre de followers")
        plt.ylabel("popularity")
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