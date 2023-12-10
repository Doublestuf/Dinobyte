import pygame as pg
#import pygame

class Cursor:
    def __init__(self) -> None:
        self.rect = pg.Rect(0, 0, 10, 10)
        #create custom cursor rect
        
        pg.mouse.set_visible(False)
        #hide default mouse cursor
    
    def update(self) -> None:
        self.rect.topleft = pg.mouse.get_pos()
        #set custom cursor position to default cursor position
    
    def draw(self, surface:pg.Surface, color:pg.Color) -> None:
        if not pg.mouse.get_focused():
            return
        #do not draw custom cursor if mouse is off-screen
        
        pg.draw.rect(surface, color, self.rect)
        #draw custom cursor rect