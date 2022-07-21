import pygame
from pygame.sprite import Sprite 


class Bliz:
    """A class to initialize Bliz (Enemy One)"""
    def __init__(self, dd_game):
        
        # Sets screen/surface 
        self.screen = dd_game.screen
        self.screen_rect = dd_game.screen.get_rect()
        
        #Load the image
        self.blizload = pygame.image.load('bliz3.png')
        
        #Get rectangle for image
        self.rect = self.blizload.get_rect()
        
        #Set x,y to float of rect
        #self.x = float(self.rect.x)
        #self.y = float(self.rect.y)
        
        """Placeholder location for image"""
        self.rect.x = 500
        self.rect.y = 500
        
    def update(self):
        """Update movement"""
        return
       # self.rect.x = self.x
        #self.rect.y = self.y
        #TD: need to reverse direction when in contact with wall
        #TD: need to have speed 
    
    def draw(self):
        """ Draw Bliz on screen """
        """Placeholder for image blit """
        self.screen.blit(self.blizload, self.rect)