import pygame as pg
#import pygaame

class Entity:
    def __init__(self, width:float, height:float, x:float, y:float) -> None:
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        #set entity rect's size and location
        
    def update(self) -> None:
        pass
    
    def draw(self, surface:pg.Surface, color:pg.Color) -> None:
        pg.draw.rect(surface, color, self.rect)
        #draw entity rect to designated surface