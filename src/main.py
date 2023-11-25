from src.view.BoardView import BoardView
from src.view.MainMenuView import MainMenu
if __name__ == '__main__':
    while(True):
        menu = MainMenu()
        menu.print_select_option()