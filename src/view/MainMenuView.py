from src.controller.MenuController import MenuController as MC


class MainMenu:

    def print_select_option(self):
        print(f"Bienvenido al buscaminas de Lucas y Saul!!")
        print(f"1 - Jugar!")
        print(f"2 - Ver ranking!")
        print(f"3 - Salir")
        user_input = int(input(f"Seleccione una opción: "))
        # Handle user input
        MC.handle_principal_input(self, user_input)
