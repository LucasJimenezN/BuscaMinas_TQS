from src.view.PlayingMenu import PlayingMenu as PM
from src.view.RankingMenu import RankingMenu as RM


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
        return True;
