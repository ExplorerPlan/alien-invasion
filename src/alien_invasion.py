import pygame as pg
from pygame.sprite import Group

from settings import Settings
from game_stats import GameStats
from src.button import Button
from ship import Ship
from scoreboard import Scoreboard
from src import game_functions as gf


def run_game():
    # initialize the game and create a screen object
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pg.display.set_caption("Alien Invasion")

    # draw a Play button and a Continue button
    play_button = Button(ai_settings, screen, "Play")
    continue_button = Button(ai_settings, screen, "Continue")

    # create a ship
    ship = Ship(ai_settings, screen)

    # create a group of bullets
    bullets = Group()

    # create a group of aliens
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # create statics and scoreboard
    stats = GameStats(ai_settings, "Hard")
    sb = Scoreboard(ai_settings, screen, stats)

    # begin the main loop of the game
    while True:
        gf.check_events( ai_settings, screen, stats, play_button, ship, aliens, bullets, sb )
        if stats.game_active and not stats.paused:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)

        gf.update_screen( ai_settings, screen, stats, sb, ship, aliens, bullets, play_button, continue_button )


run_game()
