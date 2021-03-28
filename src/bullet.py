import pygame as pg
from pygame.sprite import Sprite


class Bullet( Sprite ):
    """a class for the ship's bullets"""
    def __init__( self, ai_settings, screen, ship ):
        """create a bullet at the ship's position"""
        super().__init__()
        self.screen = screen

        # create a rectangle to represent the bullet
        self.rect = pg.Rect( 0, 0, ai_settings.bullet_width, ai_settings.bullet_height )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the position of the bullet
        self.y = float(self.rect.top)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """"move up the bullet"""
        # update the value of the position of the bullet
        self.y -= self.speed_factor
        # update the position of the rectangle
        self.rect.y = self.y

    def draw_bullet( self ):
        """draw the bullet on the screen"""
        pg.draw.rect( self.screen, self.color, self.rect )
