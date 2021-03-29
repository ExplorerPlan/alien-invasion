import json


class Settings:
    """store all the settings"""

    def __init__( self ):
        """ settings for initialization"""
        # load settings
        settings_list = self.load_data()

        # set the screen
        for settings_elem in settings_list:
            if settings_elem["ObjName"] == "Screen":
                screen_settings = settings_elem
                break
        self.screen_width = int(screen_settings["ScreenWidth"])
        self.screen_height = int(screen_settings["ScreenHeight"])
        self.bg_color = \
            (int(screen_settings["BackgroundColor_R"]),
             int(screen_settings["BackgroundColor_G"]),
             int(screen_settings["BackgroundColor_B"]))

        #  settings for the ship
        for settings_elem in settings_list:
            if settings_elem["ObjName"] == "Ship":
                ship_settings = settings_elem
                break
        self.ship_limit = int(ship_settings["ShipLimit"])

        # settings for the bullets
        for settings_elem in settings_list:
            if settings_elem["ObjName"] == "Bullet":
                bullet_settings = settings_elem
                break
        self.bullet_width = int(bullet_settings["BulletWidth"])
        self.bullet_height = int(bullet_settings["BulletHeight"])
        self.bullet_color = \
            (int(bullet_settings["BulletColor_R"]),
             int(bullet_settings["BulletColor_G"]),
             int(bullet_settings["BulletColor_B"]))
        self.bullets_allowed = int(bullet_settings["BulletAllowed"])

        # settings for the aliens
        for settings_elem in settings_list:
            if settings_elem["ObjName"] == "Alien":
                alien_settings = settings_elem
                break
        self.fleet_drop_speed = int(alien_settings["FleetDropSpeed"])

        # the scale of speeding-up and score increasing
        for settings_elem in settings_list:
            if settings_elem["ObjName"] == "Scale":
                scale_settings = settings_elem
                break
        self.speedup_scale = float(scale_settings["SpeedupScale"])
        self.score_scale = float(scale_settings["ScoreScale"])

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings( self ):
        """initialize dynamic settings"""
        # load settings
        settings_list = self.load_data()
        for settings_elem in settings_list:
            if settings_elem["ObjName"] == "DynamicSettings":
                dynamic_settings = settings_elem
                break
        self.ship_speed_factor = float(dynamic_settings["ShipSpeedFactor"])
        self.bullet_speed_factor = int(dynamic_settings["BulletSpeedFactor"])
        self.alien_speed_factor = int(dynamic_settings["AlienSpeedFactor"])

        # fleet_direction == 1 for right, -1 for left
        self.fleet_direction = int(dynamic_settings["FleetDirection"])

        # record score
        self.alien_points = int(dynamic_settings["AlienPoints"])

    def increase_speed( self ):
        """increase speed and the bonus"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    @staticmethod
    def load_data():
        with open("../config/settings.json") as f:
            settings_list = json.load(f)
        return settings_list
