

class User:
    __name = None
    __score = None

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