from engine import *
#import from engine to use in child scene classses

from src.UI import Cursor
#import custom cursor class

cursor = Cursor()
#initialize cursor
    
class Scene:
    def __init__(self, cursor_visible:bool=True) -> None:
        self.cursor_visible = cursor_visible
        #store whether cursor is visible
        
    def update(self):
        if self.cursor_visible:
            cursor.update()
            #update cursor position if it is visible
            
        return self
        #stay on current scene
    
    def draw(self):
        if self.cursor_visible:
            cursor.draw(window, WHITE)
            #draw cursor if it is visible