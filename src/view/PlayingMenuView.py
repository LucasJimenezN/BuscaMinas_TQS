from src.controller.BoardController import BoardController
class PlayingMenu:

    def show_playing_menu(self):
        print(f"Playing menu!!")
        user_input = 0

        while user_input < 1 or user_input > 3:
            print(f"Seleccione la dificultad: ")
            print(f"1 - Baja")
            print(f"2 - Media")
            print(f"3 - Alta")
            user_input = int(input(""))

        board_controller = BoardController(user_input)
        board_controller.start_game()

