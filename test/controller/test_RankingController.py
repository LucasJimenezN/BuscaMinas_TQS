import unittest
from unittest.mock import Mock, patch
from src.controller.RankingController import RankingController
from src.model.userData import User

class TestRankingController(unittest.TestCase):
    def setUp(self):
        # Mock object: Creando un objeto simulado de RankingController
        self.ranking_controller = RankingController()

    @patch('src.model.connection.DB.get_all_values')
    def test_get_ranking(self, mock_get_all_values):
        # Particiones equivalentes: Preparando los datos de prueba
        mock_get_all_values.return_value = [
            [1, 'User1', 100],
            [2, 'User2', 200],
            [3, 'User3', 150]
        ]

        # TDD: Llamando al método que estamos probando
        result = self.ranking_controller.get_ranking()

        # Statement Coverage, Decision Coverage, Condition Coverage: Verificando el resultado
        self.assertTrue(result)
        ranking_users = self.ranking_controller.get_ranking_users()
        self.assertEqual(len(ranking_users), 3)
        self.assertEqual(ranking_users[0].get_name(), 'User2')
        self.assertEqual(ranking_users[0].get_score(), 200)
        self.assertEqual(ranking_users[1].get_name(), 'User3')
        self.assertEqual(ranking_users[1].get_score(), 150)
        self.assertEqual(ranking_users[2].get_name(), 'User1')
        self.assertEqual(ranking_users[2].get_score(), 100)

    @patch('src.model.connection.DB.get_all_values')
    def test_get_ranking_with_exception(self, mock_get_all_values):
        # Valores límite y frontera: Preparando los datos de prueba
        mock_get_all_values.side_effect = Exception('Database error')

        # TDD: Llamando al método que estamos probando
        result = self.ranking_controller.get_ranking()

        # Statement Coverage, Decision Coverage, Condition Coverage: Verificando el resultado
        self.assertFalse(result)
        self.assertEqual(self.ranking_controller.get_ranking_users(), [])

if __name__ == '__main__':
    unittest.main()
