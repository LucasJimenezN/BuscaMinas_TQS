class PlayingMenuController:
    difficulty = None

    def handle_difficulty(self, option):
        # We check input types
        if not isinstance(option, int):
            return False
        # We check if option is bool, due to bools are represented as 0, 1 -> int
        if isinstance(option, bool):
            return False

        # We check limit values
        if option < 1 or option > 3:
            return False

        self.difficulty = option
        return True
