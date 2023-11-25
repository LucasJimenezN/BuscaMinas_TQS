from src.controller.BoardController import BoardController


class PlayingMenu:

    def show_playing_menu(self):
        print(f"Playing menu!!")
        user_input = None

        # While to make the user input the correct value from 1 to 3
        while user_input not in [1, 2, 3]:
            print(f"Seleccione la dificultad: ")
            print(f"1 - Baja")
            print(f"2 - Media")
            print(f"3 - Alta")
            try:
                user_input = int(input(""))
                if user_input not in [1, 2, 3]: # Check if the user put a valid number
                    print("Por favor, introduce un número entre 1 y 3.")
            except ValueError:
                # Handle exceptions
                print("Por favor, introduce un número válido.")

        # Initialize the class with the difficulty selected by the user
        board_controller = BoardController(user_input)
        # Call the method to start the game
        board_controller.start_game()
