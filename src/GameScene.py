from src.Scene import *
from src.Player import Player

class GameScene(Scene):
    def __init__(self, menu_scene) -> None:
        self.menu_scene = menu_scene
        
        super().__init__(True)
        
    def update(self):
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            return self.menu_scene
        
        return super().update()
    
    def draw(self):
        
        super().draw()