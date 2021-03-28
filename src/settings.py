class Settings:
    """store all the settings"""

    def __init__(self):
        """ settings for initialization"""
        # set the screen
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        #  settings for the ship
        self.ship_limit = 2

        # settings for the bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # settings for the aliens
        self.fleet_drop_speed = 10

        # the scale of speeding-up
        self.speedup_scale = 1.1

        #the scale of score increasing
        self.score_scale = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings( self ):
        """initialize dynamic settings"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        # fleet_direction == 1 for right, -1 for left
        self.fleet_direction = 1

        # record score
        self.alien_points = 10

    def increase_speed( self ):
        """increase speed and the bonus"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
