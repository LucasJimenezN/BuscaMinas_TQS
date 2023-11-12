from ...src.model.connection import DB


class User:
    __id = None
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

    def get_data_from_id(self, id):
        if isinstance(id, int):
            result = DB.read_value_from_id(self, id)

            if result is not None and len(result) > 0:
                """
                self.__id = result[0]
                self.__name = result[1]
                self.__score = result[2]
                """
                self.__id = result[0][0]
                self.__name = result[0][1]
                self.__score = result[0][2]
                return result

        return False
