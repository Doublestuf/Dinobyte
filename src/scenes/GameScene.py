from src.scenes.Scene import *
#import parent scene class

from src.Player import Player
#import player class

class GameScene(Scene):
    def __init__(self, menu_scene) -> None:
        self.menu_scene = menu_scene
        #store menu scene to switch between
        
        self.player = Player(30, 30, 640, 640)
        #initialize player
        
        super().__init__(True)
        #initialize parent scene class with visible cursor
        
    def update(self):
        if pg.key.get_pressed()[pg.K_ESCAPE]:
            return self.menu_scene
            #switch between game and menu scene with ESCAPE
        
        dt = clock.tick(fps) / 1000
        #calculate delta time
        
        self.player.update(dt)
        #allow player to move independent of frame rate
        
        return super().update()
        #update parent scene class
    
    def draw(self):
        self.player.draw(window, WHITE)
        #draw player
        
        super().draw()
        #draw cursor in parent scene class