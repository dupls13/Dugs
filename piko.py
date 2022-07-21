import pygame 
from settings import Settings

class Piko:
    """ A class to initialize Piko (Player) """
    
    def __init__(self, dd_game):
        """ Initializes player and defines player settings"""
        
        # Sets screen/surface 
        self.settings = dd_game.settings 
        self.screen = dd_game.screen
        self.screen_rect = dd_game.screen.get_rect()
        
        """Placeholder Image""" 
        
        # Load image
        self.pikoload = pygame.image.load('bliz.png')
        self.pikotrans = pygame.transform.scale(self.pikoload, (70,70))
        self.pikoimage = self.pikotrans 
        
        
        # Rotation variables
        self.pikoright = self.pikoimage
        self.pikoleft = pygame.transform.flip(self.pikoimage, True, False)
        self.pikodown = pygame.transform.rotate(self.pikoimage, 270)
        self.pikoup = pygame.transform.rotate(self.pikoimage, 90)
        
        self.current_face = self.pikoright
        
        
        # Get rect for image 
        self.rect = self.pikotrans.get_rect()
        
        # Set original position 
        self.rect.midtop = self.screen_rect.midtop
        
        # Decimal value for player x and y value 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # Movement flags
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False 
        
               
    def update(self):
        """ Update player position based on movement flags """
        if self.move_left and self.rect.left > 0:
            self.x -= 1
        elif self.move_right and self.rect.right < self.settings.SCREEN_WIDTH:
            self.x += 1
        elif self.move_up and self.rect.top > 0:
            self.y -= 1
        elif self.move_down and self.rect.bottom < self.settings.SCREEN_HEIGHT:
            self.y += 1

        self.rect.x = self.x
        self.rect.y = self.y
    
    def draw(self):
        """ Draws player onto screen """
        self.screen.blit(self.pikoimage, self.rect)