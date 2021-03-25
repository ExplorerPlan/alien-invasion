class Settings:
    """store all the settings"""

    def __init__(self):
        """ settings for initialization"""
        # set the screen
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        #  settings for the ship
        self.ship_speed_factor = 1

        # settings for the bullets
        self.bullet_speed_factor = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
