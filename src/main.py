from src.model.connection import DB

if __name__ == '__main__':
    database = DB()

    database.create_table()
    #database.add_values("Lucas", 1000)
    #database.get_data()