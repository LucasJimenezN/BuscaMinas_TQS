from src.view.PlayingMenuView import PlayingMenu as PM
from src.view.RankingMenuView import print_ranking
from src.controller.Exit import end_execution
from src.controller.RankingController import RankingController


class MenuController:

    def handle_principal_input(self, option):
        if not isinstance(option, int):
            return False

        if option < 1 or option > 3:
            return False

        if option == 1:
            PM.show_playing_menu(self)
        if option == 2:
            rank = RankingController()
            rank.get_ranking()
            print_ranking(rank)
        if option == 3:
            print(f"Gracias por jugar! :D")
            end_execution()

        return True;
