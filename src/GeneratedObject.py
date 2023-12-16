import pygame as pg
#import pygame for rectangle and drawing of rectangle

from engine import *
#import colors from engine.py

class GeneratedObject:
    def __init__(self, x:int, y:int, size:int) -> None:
        self.rect = pg.Rect(0, 0, size, size)
        self.rect.topleft = (x, y)
        #set the tree's size and position according to arguments in initialization
    
    def draw(self, surface:pg.Surface, color:pg.Color) -> None:
        pg.draw.rect(surface, color, self.rect)
        #draw the tree's rect to its designated surface