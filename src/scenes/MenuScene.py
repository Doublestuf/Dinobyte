from src.scenes.GameScene import GameScene
from src.scenes.Scene import *

class MenuScene(Scene):
    def __init__(self) -> None:
        super().__init__(True)
        title_font = pg.font.Font(default_font_name, 200)
        self.title_text = title_font.render("Dinobyte", False, WHITE)
        
        self.title_text_rect = self.title_text.get_rect()
        self.title_text_rect.centerx = window.get_rect().centerx
        self.title_text_rect.top = 100
        
        start_font = pg.font.Font(default_font_name, 50)
        self.start_text = start_font.render("Press to Start", False, WHITE)
        
        self.start_text_rect = self.start_text.get_rect()
        self.start_text_rect.centerx = window.get_rect().centerx
        self.start_text_rect.top = self.title_text_rect.bottom + 100
        
    def update(self):
        if cursor.rect.colliderect(self.start_text_rect) and pg.event.get(pg.MOUSEBUTTONDOWN):
            return GameScene(self)

        return super().update()
    
    def draw(self):
        window.blit(self.title_text, self.title_text_rect)
        window.blit(self.start_text, self.start_text_rect)
        
        super().draw()