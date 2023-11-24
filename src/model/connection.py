import sqlite3


class DB:
    CONST_DATABASE_NAME = "model/data.db"
    CONST_TABLE_NAME = 'users'

    def create_table(self):
        conn = sqlite3.connect(self.CONST_DATABASE_NAME)
        try:
            conn.execute("""create table users (
                              id integer primary key autoincrement,
                              user_name text,
                              user_score integer
                        )""")
        except sqlite3.OperationalError:
            pass
        conn.close()

    def create_values(self, name, score):
        if not isinstance(name, str):
            print("Error: El nombre debe ser un string.")
            return False
        if not isinstance(score, int):
            print("Error: La puntuación debe ser un entero.")
            return False
        try:
            conn = sqlite3.connect(self.CONST_DATABASE_NAME)
            cursor = conn.cursor()
            insert_query = 'INSERT INTO users (user_name, user_score) VALUES (?, ?)'
            cursor.execute(insert_query, (name, score))
            conn.commit()
        except sqlite3.IntegrityError:
            print("Error: El valor que intentas insertar en 'user_name' ya existe en la base de datos.")
            return False
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            if conn:
                conn.close()
        return True

    def read_all_values(self):
        try:
            conn = sqlite3.connect(self.CONST_DATABASE_NAME)
            cur = conn.execute("select * from users")
            print("select * from " + self.CONST_TABLE_NAME)
            # print data using cursor object
            for i in cur:
                print(i[0], " ", i[1], " ", i[2])
        except sqlite3.Error as e:
            print(f"Error: {e}")
            return False
        finally:
            if conn:
                conn.close()
        return True

    def get_all_values(self):
        try:
            conn = sqlite3.connect(self.CONST_DATABASE_NAME)
            cur = conn.execute("select * from users")
            data = cur.fetchall()
            conn.close()
        except sqlite3.Error as e:
            return False
        return data

    def read_value_from_id(self, id):
        data = None
        if id is not None:
            if isinstance(id, int):
                # Here we get the value if possible
                conn = (sqlite3.connect
                        (self.CONST_DATABASE_NAME))
                cur = conn.execute("select * from users where id=?", (id,))

                result = cur.fetchall()
                cur.close()
                conn.close()

                if result is not None:
                    return result
        return False

    def delete_value_from_id(self, id):
        if id is not None and isinstance(id, int):
            try:
                conn = sqlite3.connect(self.CONST_DATABASE_NAME)
                cursor = conn.cursor()
                delete_query = 'DELETE FROM users WHERE id = ?'
                cursor.execute(delete_query, (id,))
                conn.commit()
            except sqlite3.Error as e:
                print(f"Error: {e}")
                return False
            finally:
                if conn:
                    conn.close()
            return True

    def check_insert_data(self, name, score):
        if name is not None and score is not None:
            if isinstance(name, str) and isinstance(score, int):
                return True
        return False
