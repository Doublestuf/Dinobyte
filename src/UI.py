import pygame as pg
#imports

class Cursor:
    def __init__(self) -> None:
        self.rect = pg.Rect(0, 0, 10, 10)
        
        pg.mouse.set_visible(False)
    
    def update(self) -> None:
        self.rect.topleft = pg.mouse.get_pos()
    
    def draw(self, surface, color) -> None:
        if not pg.mouse.get_focused():
            return
        pg.draw.rect(surface, color, self.rect)