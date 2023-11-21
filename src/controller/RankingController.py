from src.model.connection import DB
from src.model.userData import User


class RankingController:
    __ranking_users = []
    __db = DB()

    def get_ranking(self):
        try:
            aux = self.__db.get_all_values()
            for user in aux:
                aux_user = User()
                aux_user.set_id(user[0])
                aux_user.set_name(user[1])
                aux_user.set_score(user[2])
                self.__ranking_users.append(aux_user)
        except Exception as e:
            print(f"Error: {e}")
            return False
        return True

    def print_ranking(self):
        for users in self.__ranking_users:
            print(f"Id: {users.get_id()} / Name: {users.get_name()} / Score: {users.get_score()}")

