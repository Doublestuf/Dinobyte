from engine import *
#import needed variables from engine.py

from src.Player import Player
from src.UI import Cursor
#import game objects

from src.Generator import Generator
#import object generator

from src.MenuScene import MenuScene
#import scenes

player = Player(30, 30, 640, 360)
cursor = Cursor()
#initialize game objects

generator = Generator()
#initialize object generator

current_scene = MenuScene()

def update(dt:float):
    player.update(dt)
    #player requires delta time to normalize movement speed
    
    cursor.update()
#update all game objects in one function

def draw():
    player.draw(window, WHITE)
    #draw game objects first
    
    cursor.draw(window, WHITE)
    #draw UI on top of game objects
    
#draw all game objects in one function

while True:
    if pg.event.get(pg.QUIT) or pg.key.get_pressed()[pg.K_ESCAPE]:
        break
    #exit program when window is closed or ESCAPE key is pressed
    
    window.fill(BLACK)
    #clear screen each frame
    
    dt = clock.tick(fps) / 1000
    #calculate time between frames
    
    current_scene = current_scene.update()
    current_scene.draw()
    #update and draw all objects/sprites
    
    pg.display.update()
    #show changes and restrict framerate
#game loop