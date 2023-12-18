from src.scenes.GameScene import GameScene
#import game scene to switch to after pressing play

from src.scenes.Scene import *
#import from parent scene class for cursor updates and other

class MenuScene(Scene):
    def __init__(self) -> None:
        super().__init__(True)
        #initialize parent scene class with cursor visible
        
        title_font = pg.font.Font(default_font_name, 200)
        #create big font for title text
        
        self.title_text = title_font.render("Dinobyte", False, WHITE)
        #create text surface for the game title
        
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.centerx = window.get_rect().centerx
        self.title_text_rect.top = 100
        #set position of the game title text
        
        start_font = pg.font.Font(default_font_name, 50)
        #create smaller font for start text
        
        self.start_text = start_font.render("Press to Start", False, WHITE)
        #create text surface for starting text
        
        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.centerx = window.get_rect().centerx
        self.start_text_rect.top = self.title_text_rect.bottom + 100
        #set position of the starting text
        
    def update(self):
        if cursor.rect.colliderect(self.start_text_rect) and pg.event.get(pg.MOUSEBUTTONDOWN):
            return GameScene(self)
            #change scene to gamescene if player clicks on start text

        return super().update()
        #stay on current scene if player does not click
    
    def draw(self):
        window.blit(self.title_text, self.title_text_rect)
        window.blit(self.start_text, self.start_text_rect)
        #draw game title and start text to screen
        
        super().draw()
        #draw cursor in parent scene class