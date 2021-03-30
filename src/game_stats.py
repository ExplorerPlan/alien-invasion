import json


class GameStats:
    """ track the statistical info """

    def __init__(self, ai_settings, game_mode):
        """ initialize the statics """
        self.ai_settings = ai_settings
        self.game_mode = game_mode
        self.reset_stats()
        self.game_active = False
        self.paused = False
        self.high_score = self.load_high_score(game_mode)

    def reset_stats( self ):
        """initialize the statics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

    @staticmethod
    def load_high_score( game_mode ):
        with open("../config/high_score.json") as f:
            high_score_list = json.load(f)
            for score in high_score_list:
                if score["GameMode"] == game_mode:
                    high_score = int(score["Score"])
        return high_score
