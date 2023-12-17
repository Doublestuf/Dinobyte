import pygame as pg

from engine import *

from src.UI import Cursor

cursor = Cursor()
    
class Scene:
    def __init__(self, cursor_visible:bool=True) -> None:
        self.cursor_visible = cursor_visible
        
    def update(self):
        if pg.event.get(pg.QUIT):
            pg.quit()
        
        if self.cursor_visible:
            cursor.update()
            
        return self
    
    def draw(self):
        if self.cursor_visible:
            cursor.draw(window, WHITE)