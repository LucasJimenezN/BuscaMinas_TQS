import unittest
from unittest.mock import Mock, patch, MagicMock, call
from src.controller.BoardController import BoardController


class TestBoardController(unittest.TestCase):
    def setUp(self):
        # Mock object: Creando un objeto simulado de BoardController
        self.board_controller = BoardController(1)

    @patch('src.controller.BoardController.input', create=True)
    @patch('src.model.userData.User.add_user', return_value=None)
    def test_play_game(self, mocked_add_user, mocked_input):
        # Particiones equivalentes: Preparando los datos de prueba
        mocked_input.side_effect = ['A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1']

        # Mock object: Simulando los métodos de la clase Board
        self.board_controller.board.is_game_won = MagicMock(side_effect=[False] * 15 + [True])
        self.board_controller.board.is_game_lost = False

        # TDD: Llamando al método que estamos probando
        self.board_controller.play_game()

        # Statement Coverage, Decision Coverage, Condition Coverage: Verificando el resultado
        self.board_controller.board.is_game_won.assert_has_calls([call()] * 16)

    @patch('src.controller.BoardController.input', create=True)
    def test_play_game_with_invalid_input(self, mocked_input):
        # Valores límite y frontera: Preparando los datos de prueba
        mocked_input.side_effect = ['Z', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1', 'A', '1']

        # Mock object: Simulando los métodos de la clase Board
        self.board_controller.board.is_game_won = MagicMock(side_effect=[False] * 15 + [True])
        self.board_controller.board.is_game_lost = False

        # TDD: Llamando al método que estamos probando
        self.board_controller.play_game()

        # Statement Coverage, Decision Coverage, Condition Coverage: Verificando el resultado
        self.board_controller.board.is_game_won.assert_has_calls([call()] * 16)

if __name__ == '__main__':
    unittest.main()
