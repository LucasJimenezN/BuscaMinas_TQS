from src.model.connection import DB
from src.model.userData import User


class RankingController:
    __ranking_users = []
    __db = DB()

    def get_ranking_users(self):
        return self.__ranking_users

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
        self.sort_ranking()
        return True

    def sort_ranking(self):
        self.__ranking_users.sort(key=lambda user: user.get_score(), reverse=True)
