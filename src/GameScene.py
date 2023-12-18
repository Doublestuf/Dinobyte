from src.Scene import *
from src.Player import Player

class GameScene(Scene):
    def __init__(self, menu_scene) -> None:
        self.menu_scene = menu_scene
        
        self.player = Player(30, 30, 640, 640)
        
        super().__init__(True)
        
    def update(self):
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            return self.menu_scene
        
        dt = clock.tick(fps) / 1000
        
        self.player.update(dt)
        
        return super().update()
    
    def draw(self):
        self.player.draw(window, WHITE)
        
        super().draw()