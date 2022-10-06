import sqlite3
from sqlite3 import Error


def create_connection(db_file):

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


        

if __name__ == '__main__':
    main()

#### A ENTRER DANS LE TERMINAL :
# sqlite3 d:\sqlite\db\pythonsqlite.db
# .header on
# .mode column
# SELECT * FROM projects;
