from engine import *
#import needed variables from engine.py

from src.Player import Player
from src.UI import Cursor
#import game objects

player = Player(30, 30, 640, 360)
cursor = Cursor()
#initialize game objects

def update(dt):
    player.update(dt)
    #player requires delta time to normalize movement speed
    
    cursor.update()
#update all game objects in one function

def draw():
    player.draw(window, WHITE)
    cursor.draw(window, WHITE)
#draw all game objects in one function

while True:
    if pg.event.get(pg.QUIT) or pg.key.get_pressed()[pg.K_ESCAPE]:
        break
    #exit program when window is closed or ESCAPE key is pressed
    
    window.fill(BLACK)
    #clear screen each frame
    
    dt = clock.tick(fps) / 1000
    
    update(dt)
    draw()
    #update and draw all objects/sprites
    
    pg.display.update()
    #show changes and restrict framerate
#game loop