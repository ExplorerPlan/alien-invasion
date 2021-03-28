class GameStats:
    """ track the statistical info """

    def __init__(self, ai_settings):
        """ initialize the statics """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats( self ):
        """initialize the statics"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
