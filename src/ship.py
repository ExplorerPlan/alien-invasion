import pygame as pg
from pygame.sprite import Sprite


class Ship( Sprite ):
    def __init__( self, ai_settings, screen ):
        """initialize the ship and its initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of the ship
        self.image = pg.image.load( '../images/ship.bmp' )
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # put the ship on the bottom of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store small number in center factor
        self.centerx = float( self.rect.centerx )
        self.centery = float( self.rect.centery )

        #signals for movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update( self ):
        """respond to the events"""
        if self.moving_right and self.rect.centerx < 1251:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.centerx > 29:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.centery > 24:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.centery < 696:
            self.centery += self.ai_settings.ship_speed_factor
        #update rect object with center value
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme( self ):
        """draw the ship at the specific position"""
        self.screen.blit( self.image, self.rect )

    def center_ship( self ):
        """put ship in the centre"""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - self.rect.height
