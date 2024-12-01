from entities.game_stats import GameStats


class GameStatsService:
    def __init__(self, game_stats_repo):
        self.game_stats_repo = game_stats_repo

    def add_game_stats(
            self, id, user_id, opponent, date, goals, assists, play_time, rating, feedback):
        game_stats = GameStats(id, user_id, opponent,
                               date, goals, assists, play_time, rating, feedback)
        self.game_stats_repo.add_game_stats(game_stats)
        return True, "Pelitilasto lisätty!"

    def get_game_stats(self, user_id):
        return self.game_stats_repo.get_game_stats(user_id)

    def delete_game_stat(self, stat_id):
        self.game_stats_repo.delete_game_stat(stat_id)
