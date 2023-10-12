import sqlite3
from itertools import islice

class DB:
    #Here we should change the databse path if saul or lucas is executing
    LUCAS_DATABASE_PATH = r"/Users/lucasjimeneznunez/Desktop/UAB/4t/TQS/Practicas/P1/Project_Python/src/model/data.db"
    CONST_DATABASE_NAME = LUCAS_DATABASE_PATH
    CONST_TABLE_NAME = 'users'

    def create_table(self):
        conn = sqlite3.connect(self.CONST_DATABASE_NAME)
        try:
            conn.execute("""create table users (
                              id integer primary key autoincrement,
                              user_name text unique,
                              user_score integer
                        )""")
            print("Table created")
        except sqlite3.OperationalError:
            print("Table already exist")
        conn.close()

    def create_values(self, name, score):
        conn = sqlite3.connect(self.CONST_DATABASE_NAME)
        cursor = conn.cursor()
        insert_query = 'INSERT INTO users (user_name, user_score) VALUES (?, ?)'
        cursor.execute(insert_query, (name, score))
        conn.commit()
        conn.close()

    def read_all_values(self):
        conn = sqlite3.connect(self.CONST_DATABASE_NAME)
        cur = conn.execute("select * from users")
        print("select * from " + self.CONST_TABLE_NAME)
        # print data using cursor object
        for i in cur:
            print(i[0], " ", i[1], " ", i[2])
        conn.close()
        
    def read_value_from_id(self, id):
        data = None
        if id is not None:
            if isinstance(id, int):
                # Here we get the value if possible
                conn = (sqlite3.connect
                        (r"/Users/lucasjimeneznunez/Desktop/UAB/4t/TQS/Practicas/P1/Project_Python/src/model/data.db"))
                cur = conn.execute("select * from users where id=?", (id,))

                result = cur.fetchall()
                cur.close()
                conn.close()

                if result is not None:
                    return result
        return False

    def update_value(self):
        pass

    def delete_value(self):
        pass

    def delete_value(self, id):
        pass

    def check_insert_data(self, name, score):
        if name is not None and score is not None:
            if isinstance(name, str) and isinstance(score, int):
                return True
        return False