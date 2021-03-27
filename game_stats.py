class GameStats:
    """ track the statistical info """

    def __init__(self, ai_settings):
        """ initialize the statics """
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

    def reset_stats( self ):
        """initialize the statics"""
        self.ships_left = self.ai_settings.ship_limit
