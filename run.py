from engine import *
#import from engine for window, colors, etc

from src.scenes.MenuScene import MenuScene
#import menuscene to start the game on

current_scene = MenuScene()
#set default scene to menu scene

while True:
    if pg.event.get(pg.QUIT):
        break
    #exit program when window is closed

    window.fill(BLACK)
    #clear screen each frame

    current_scene = current_scene.update()
    #update scene and change scene if needed
    
    current_scene.draw()
    #draw objects in the current scene
    
    pg.display.update()
    #show changes
#game loop