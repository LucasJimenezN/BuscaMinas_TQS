from src.model.connection import DB
from src.view.MainMenuView import main_menu as MM

if __name__ == '__main__':

    menu = MM()
    menu.print_select_option()