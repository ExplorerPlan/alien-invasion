import pygame as pg
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # initialize the game and create a screen object
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)

    # create a group of bullets
    bullets = Group()

    # create a group of aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # create statics
    stats = GameStats(ai_settings)

    # begin the main loop of the game
    while True:
        gf.check_events( ai_settings, screen, ship, bullets )
        ship.update()
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen( ai_settings, screen, ship, aliens, bullets )


run_game()
