import sys

import pygame as pg
from bullet import Bullet


def fire_bullet( ai_settings, screen, ship, bullets ):
    if len( bullets ) < ai_settings.bullets_allowed:
        new_bullet = Bullet( ai_settings, screen, ship )
        bullets.add( new_bullet )


def check_keydown_events(event, ai_settings, screen, ship, bullets ):
    """respond to the keydown events"""
    if event.key == pg.K_RIGHT:
        ship.moving_right = True
    elif event.key == pg.K_LEFT:
        ship.moving_left = True
    elif event.key == pg.K_UP:
        ship.moving_up = True
    elif event.key == pg.K_DOWN:
        ship.moving_down = True
    elif event.key == pg.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """respond to the keyup events"""
    if event.key == pg.K_RIGHT:
        ship.moving_right = False
    elif event.key == pg.K_LEFT:
        ship.moving_left = False
    elif event.key == pg.K_UP:
        ship.moving_up = False
    elif event.key == pg.K_DOWN:
        ship.moving_down = False


def check_events(ai_settings, screen, ship, bullets ):
    """check clicks and mouse events"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)


def update_screen( ai_settings, screen, ship, bullets ):
    """update the image on the screen and switch to the new screen"""
    # redraw the screen every loop
    screen.fill(ai_settings.bg_color)

    #redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    ship.blitme()

    # make the screen visible
    pg.display.flip()


def update_bullets(bullets):
    """update the positions of the bullets and delete vanished bullets"""
    # update the positions of bullets
    bullets.update()

    # delete all the vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom < 1:
            bullets.remove( bullet )
