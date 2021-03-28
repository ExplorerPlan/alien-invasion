import sys
from time import sleep

import pygame as pg
from bullet import Bullet
from alien import Alien


def start_game(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """start a new game"""
    # set game active and reset the settings and stats
    stats.game_active = True
    ai_settings.initialize_dynamic_settings()
    stats.reset_stats()

    # empty aliens and bullets
    aliens.empty()
    bullets.empty()

    # create a new fleet of aliens and set ship to the center
    create_fleet( ai_settings, screen, ship, aliens )
    ship.center_ship()

    # set mouse invisible
    pg.mouse.set_visible( False )

    # reset the scoreboard
    sb.prep_score()
    sb.prep_high_score()
    sb.prep_level()
    sb.prep_ships()


def fire_bullet( ai_settings, screen, ship, bullets ):
    if len( bullets ) < ai_settings.bullets_allowed:
        new_bullet = Bullet( ai_settings, screen, ship )
        bullets.add( new_bullet )


def check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb ):
    """check clicks and mouse events"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, ai_settings, stats, screen, ship, aliens, bullets, sb)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pg.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, mouse_x, mouse_y)


def check_keydown_events(event, ai_settings, stats, screen, ship, aliens, bullets, sb ):
    """respond to the keydown events"""
    if event.key == pg.K_d:
        ship.moving_right = True
    elif event.key == pg.K_a:
        ship.moving_left = True
    elif event.key == pg.K_w:
        ship.moving_up = True
    elif event.key == pg.K_s:
        ship.moving_down = True
    elif event.key == pg.K_SPACE:
        if stats.game_active:
            fire_bullet(ai_settings, screen, ship, bullets)
        else:
            start_game(ai_settings, stats, screen, ship, aliens, bullets, sb)
    elif event.key == pg.K_ESCAPE:
        sys.exit()


def check_keyup_events(event, ship):
    """respond to the keyup events"""
    if event.key == pg.K_d:
        ship.moving_right = False
    elif event.key == pg.K_a:
        ship.moving_left = False
    elif event.key == pg.K_w:
        ship.moving_up = False
    elif event.key == pg.K_s:
        ship.moving_down = False


def check_play_button(ai_settings, screen, stats, play_button, ship, aliens, bullets, sb, mouse_x, mouse_y):
    """when clicked Play, start new game"""
    if play_button.rect.collidepoint(mouse_x, mouse_y) and not stats.game_active:
        start_game(ai_settings, stats, screen, ship, aliens, bullets, sb)


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """ check if some bullet collide aliens"""
    # if so, delete the bullet and the alien
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # delete current bullets and reset a new fleet of aliens
        bullets.empty()
        ai_settings.increase_speed()

        # upgrade level
        stats.level += 1
        sb.prep_level()

        create_fleet(ai_settings, screen, ship, aliens)


def check_fleet_edges(ai_settings, aliens):
    """check if some alien touches edge"""
    for alien in aliens.sprites():
        if alien.check_edge():
            change_fleet_direction(ai_settings, aliens)
            break


def check_high_score(stats, sb):
    """check if new highest score generated"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def change_fleet_direction(ai_settings, aliens):
    """move the fleet lower and change their direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """check if there is alien at the bottom"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)
            break


def create_fleet(ai_settings, screen, ship, aliens):
    """"create a fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_aliens_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    for row_number in range(number_aliens_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """calculate the number of aliens per row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / ( 2 * alien_width)) + 1
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """calculate rows of aliens"""
    available_space_y = (ai_settings.screen_height - 3 * alien_height - ship_height)
    number_rows = int( available_space_y / (2 * alien_height) )
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """create an alien and put it in the current row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height * row_number + 60
    aliens.add( alien )


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """respond to the ship hit by alien"""
    if stats.ships_left > 0:
        # ship_left subtract 1
        stats.ships_left -= 1

        # clear the aliens and bullets
        aliens.empty()
        bullets.empty()

        # create a new fleet of aliens and reset the ship
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # upload scoreboard
        sb.prep_ships()

        # pause
        sleep(0.5)
    else:
        stats.game_active = False
        pg.mouse.set_visible(True)


def update_aliens(ai_settings, stats, screen,  ship, aliens, bullets, sb):
    """update the positions of aliens"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # check the collisions between aliens and ship
    if pg.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

    """check aliens at bottom"""
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets, sb)


def update_screen( ai_settings, screen, stats, sb, ship, aliens, bullets, play_button ):
    """update the image on the screen and switch to the new screen"""
    # redraw the screen every loop
    screen.fill(ai_settings.bg_color)

    #redraw all the bullets
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # redraw the ship and aliens
    ship.blitme()
    aliens.draw(screen)

    # show the score
    sb.show_score()

    # if not active, draw the button
    if not stats.game_active:
        play_button.draw_button()

    # make the screen visible
    pg.display.flip()


def update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets):
    """update the positions of the bullets and delete vanished bullets"""
    # update the positions of bullets
    bullets.update()

    # delete all the vanished bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom < 1:
            bullets.remove( bullet )
    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, aliens, bullets)
