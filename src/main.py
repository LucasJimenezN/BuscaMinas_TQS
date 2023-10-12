from src.model.connection import DB

if __name__ == '__main__':
    database = DB()

    database.create_table()
    #database.create_values("Saul", 100)
    database.read_all_values()