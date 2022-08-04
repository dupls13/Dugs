import pygame 

from pygame.sprite import Sprite

from piko import Piko 
from settings import Settings

class Arrow(Sprite):
    """ A class to manage arrows fired from player"""
    
    def __init__(self, dd_game):
        """ Create an arrow object at player position """
        super().__init__()
        self.screen = dd_game.screen 
        self.settings = dd_game.settings 
        
        #Load arrow image ,,, placeholder
        self.arrowload = pygame.image.laod('bullet.png')
        self.imagescale = pygame.transform.scale(self.imageload, (20, 20))
        self.rect = self.imagescale.get_rect()
        
        #Set bullet initial location 
        self.rect.midtop = dd_game.player.rect.midtop
        
        # Get rect for arrow 
        self.x = float (self.rect.x)
        self.y = float(self.rect.y)
        
        self.speed = 15
        
    def update(self):
        if """ player facing left: 
            self.x -= int(self.speed)"""
        if """ player facing right:
            self.x += int(self.speed)"""
        if """ player facing down:
            self.y -= int(self.speed)"""
        if """ player facing up:
            self.y += int(self.speed)"""