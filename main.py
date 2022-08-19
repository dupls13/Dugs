# Main file of game 

# Imports
import pygame 
import sys 

# Import files
from settings import Settings
from bliz import Bliz
from piko import Piko
from dirt import Dirt
from arrow import Arrow 


class Digdug:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and create the game resources"""
        
        # Loads Settings 
        self.settings = Settings()
        
        # Defines 'screen' and gives dimensions 
        self.screen = pygame.display.set_mode((
            self.settings.SCREEN_WIDTH, self.settings.SCREEN_HEIGHT))
        
        
        # Defines enemy character in order to load
        self.bliz = Bliz(self)
        
        # Defines player in order to load 
        self.piko = Piko(self)
        
        self.arrow = pygame.sprite.Group()
        
        #Define dirt in order to load
        self.dirt = Dirt(self)
    
    def run_game(self):
        """Start the main loop of the game"""
        while True:
            
            self.check_events()
            
            self.piko.update()
            
            self.arrow.update()
            
            
            self.update_screen()
            
    
    def check_events(self):
        """ Check events in game """
        
        for event in pygame.event.get():
            
            #Defines option to quit game 
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            # Checks event for key presses (down)
            elif event.type == pygame.KEYDOWN:
                
                # Allows 'esc' key to quit game 
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
                # Movement flags (True) and set rotation
                if event.key == pygame.K_a:
                    self.piko.move_left = True
                    self.piko.pikoimage = self.piko.pikoleft
                if event.key == pygame.K_d:
                    self.piko.move_right = True
                    self.piko.pikoimage = self.piko.pikoright  
                if event.key == pygame.K_w:
                    self.piko.move_up = True
                    self.piko.pikoimage = self.piko.pikoup
                if event.key == pygame.K_s:
                    self.piko.move_down = True
                    self.piko.pikoimage = self.piko.pikodown 
                    
                if event.key == pygame.K_SPACE:
                    new_arrow = Arrow(self)
                    self.arrow.add(new_arrow)
                    
            
            # Check event for key presses (up):
            elif event.type == pygame.KEYUP:
                
                # Movement flags (False)
                if event.key == pygame.K_a:
                    self.piko.move_left = False
                if event.key == pygame.K_d:
                    self.piko.move_right = False
                if event.key == pygame.K_w:
                    self.piko.move_up = False
                if event.key == pygame.K_s:
                    self.piko.move_down = False              
                
    def update_screen(self):
        """ Update screen with each passthrough """
        
        # Sets screen background color - TD : Change to black 
        self.screen.fill(self.settings.bg_color)
        

        # Calls Bliz function to draw enemy
        self.bliz.draw()
        self.piko.draw()
        self.dirt.drawGrid()
        for Arrow in self.arrow.sprites():
            Arrow.draw()
        
        pygame.display.flip()
        


if __name__ == '__main__':
    """Make a game instance and run the game"""
    dd = Digdug()
    dd.run_game()
    