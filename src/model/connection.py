import sqlite3
from itertools import islice


class DB:
    CONST_DATABASE_NAME = "data.db"
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

    def add_values(self, name, score):
        conn = sqlite3.connect(self.CONST_DATABASE_NAME)
        cursor = conn.cursor()
        insert_query = 'INSERT INTO users (user_name, user_score) VALUES (?, ?)'
        cursor.execute(insert_query, (name, score))
        conn.commit()
        conn.close()

    def get_data(self):
        conn = sqlite3.connect(self.CONST_DATABASE_NAME)
        cur = conn.execute("select * from users")
        print("select * from " + self.CONST_TABLE_NAME)
        # print data using cursor object
        for i in cur:
            print(i[0], " ", i[1], " ", i[2])
        conn.close()


    def check_insert_data(self, name, score):
        if name is not None and score is not None:
            if isinstance(name, str) and isinstance(score, int):
                return True
        return False