from src.model.connection import DB


class User:
    __id = None
    __name = None
    __score = None

    def get_id(self):
        return self.__id

    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if isinstance(score, int):
            self.__score = score

    def add_user(self, score):
        name = input("Tell me your name: ")
        print(f"{name} got: {score}!")
        db = DB()
        db.create_values(name, score)
