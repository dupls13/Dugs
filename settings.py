import pygame 

class Settings:
    """ A class to store all the settings for DigDug"""
    
    def __init__(self):
        """ Initialize game settings"""
        
        #   Screen Settings
        self.bg_color = (255, 255, 255)
        self.SCREEN_WIDTH = 1600
        self.SCREEN_HEIGHT = 800
        
        pygame.display.set_caption("DigDig")
    