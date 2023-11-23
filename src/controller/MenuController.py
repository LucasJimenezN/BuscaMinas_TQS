from src.view.PlayingMenuView import PlayingMenu as PM
from src.view.RankingMenuView import print_ranking as RM
from src.controller.Exit import end_execution


class MenuController:

    def handle_principal_input(self, option):
        if not isinstance(option, int):
            return False

        if option < 1 or option > 3:
            return False

        if option == 1:
            PM.show_playing_menu(self)
        if option == 2:
            RM.show_ranking_menu(self)
        if option == 3:
            print(f"Closing function")
            end_execution()

        return True;
