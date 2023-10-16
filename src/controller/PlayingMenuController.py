class PlayingMenuContoller:
    difficulty = None

    def handle_difficulty(self, option):
        if not isinstance(option, int):
            return False
        if option < 1 or option > 3:
            return False

        self.difficulty = option
        return True
