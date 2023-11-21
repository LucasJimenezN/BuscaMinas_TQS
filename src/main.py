from src.controller.RankingController import RankingController

if __name__ == '__main__':
    rank = RankingController()
    rank.get_ranking()
    rank.print_ranking()