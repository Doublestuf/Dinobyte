import pygame as pg
from engine import *
from src.Player import Player
from src.UI import Cursor
#imports

player = Player(30, 30, 640, 360)
cursor = Cursor()
#game objects

def update():
    player.update()
    cursor.update()
#add ability to update all objects

def draw():
    player.draw(window, WHITE)
    cursor.draw(window, WHITE)
#add ability to draw all objects to the screen

while True:
    keys = pg.key.get_pressed()
    
    if pg.event.get(pg.QUIT) or keys[pg.K_ESCAPE]:
        break
    #exit program when window is closed or ESCAPE key is pressed
    
    window.fill(BLACK)
    #clear screen
    
    update()
    draw()
    #update and draw all objects/sprites
    
    clock.tick(fps)
    pg.display.update()
    #show changes and restrict framerate
#game loop