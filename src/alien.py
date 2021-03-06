import pygame as pg
from pygame.sprite import Sprite


class Alien(Sprite):
    """class for a single alien"""
    def __init__(self, ai_settings, screen):
        """initialize an alien and set initial position"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the image of the alien and set its rect
        self.image = pg.image.load( '../images/alien.bmp' )
        self.rect = self.image.get_rect()

        # appear on the left top initially
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the accurate position
        self.x = float(self.rect.x)

    def blitme( self ):
        """"draw the alien at specific position"""
        self.screen.blit(self.image, self.rect)

    def update( self ):
        """move the alien to the right"""
        self.x += self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction
        self.rect.x = self.x

    def check_edge( self ):
        """if at the edge, return True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
