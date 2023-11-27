import unittest
from unittest.mock import Mock
from src.model.userData import User
from src.controller.RankingController import RankingController


class TestRankingController(unittest.TestCase):

    def test_get_ranking(self):
        ranking_controller = RankingController()
        # Mock DB method to simulate get_all_values
        ranking_controller._RankingController__db.get_all_values = Mock(return_value=[
            (1, 'Alice', 100),
            (2, 'Bob', 80),
            (3, 'Charlie', 120)
        ])

        result = ranking_controller.get_ranking()

        self.assertTrue(result)
        self.assertEqual(len(ranking_controller._RankingController__ranking_users), 3)

    def test_sort_ranking(self):
        ranking_controller = RankingController()
        ranking_controller._RankingController__ranking_users = [
            User(1, 'Alice', 100),
            User(2, 'Bob', 80),
            User(3, 'Charlie', 120)
        ]

        ranking_controller.sort_ranking()

        expected_order = [
            User(3, 'Charlie', 120),
            User(1, 'Alice', 100),
            User(2, 'Bob', 80)
        ]

        # We check all the attributes for the Users
        for i in range(len(ranking_controller._RankingController__ranking_users)):
            self.assertEqual(
                ranking_controller._RankingController__ranking_users[i].get_id(),
                expected_order[i].get_id()
            )
            self.assertEqual(
                ranking_controller._RankingController__ranking_users[i].get_name(),
                expected_order[i].get_name()
            )
            self.assertEqual(
                ranking_controller._RankingController__ranking_users[i].get_score(),
                expected_order[i].get_score()
            )


if __name__ == '__main__':
    unittest.main()
