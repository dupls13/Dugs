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
        self.arrowload = pygame.image.load('bullet.png')
        self.imagescale = pygame.transform.scale(self.arrowload, (20, 20))
        self.rect = self.imagescale.get_rect()
        
        #Set bullet initial location 
        self.rect.midtop = dd_game.piko.rect.midtop
        
        # Get rect for arrow 
        self.x = float (self.rect.x)
        self.y = float(self.rect.y)
        
        self.speed = 3
        
    def update(self):
        self.x += int(self.speed)
        self.rect.x = self.x 
        """Currently only goes to right, need to go with player direction"""
    
    def draw(self):
        #Draw arrow on screen
        self.screen.blit(self.imagescale, self.rect)