from engine import *
#import needed variables from engine.py

from src.scenes.MenuScene import MenuScene
#import scenes

current_scene = MenuScene()

while True:
    if pg.event.get(pg.QUIT):
        break
    #exit program when window is closed

    window.fill(BLACK)
    #clear screen each frame

    current_scene = current_scene.update()
    current_scene.draw()
    #update and draw all objects/sprites
    
    pg.display.update()
    #show changes
#game loop