import pygame 
from settings import Settings

#Test black
BLACK=(0,0,0)

class Dirt:
    """ Class to initialize dirt blocks """
    
    def __init__(self, dd_game):
        
        # Load game screen settings
        self.settings = dd_game.settings 
        self.screen = dd_game.screen 
        self.screen_rect = dd_game.screen.get_rect()
        
        # Load dirt images
        self.dirtLoad = pygame.image.load('dirt.png')
        self.dirtscale = pygame.transform.scale(self.dirtLoad, (70,70))
        self.dirt = self.dirtscale 
        self.rect = self.dirt.get_rect()
        
        self.dirtWidth = self.rect.width 
        self.dirtHeight = self.rect.height
        
        
    def drawGrid(self):
        blocksize = 70
        black = (0, 0, 0)
        rect = self.rect 
        for x in range(self.screen):
            pygame.draw.rect(self.dirt, self.rect)