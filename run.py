from engine import *
#import needed variables from engine.py

from src.Player import Player
from src.UI import Cursor
#import game objects

from src.Generator import Generator
#import object generator

player = Player(30, 30, 640, 360)
cursor = Cursor()
#initialize game objects

generator = Generator()
#initialize object generator

def update(dt:float):
    player.update(dt)
    #player requires delta time to normalize movement speed
    
    cursor.update()
#update all game objects in one function

def draw():
    for object in generator.generated_objects:
        object.draw(window)
    #draw all randomly generated objects such as trees and rocks
    
    player.draw(window, WHITE)
    #draw game objects first
    
    cursor.draw(window, WHITE)
    #draw UI on top of game objects
    
#draw all game objects in one function

def start_game():
    generator.generate_trees()
    #randomly generate trees when game begins

start_game()
#perform necessary functions before starting the game (start menu, etc.)

while True:
    if pg.event.get(pg.QUIT) or pg.key.get_pressed()[pg.K_ESCAPE]:
        break
    #exit program when window is closed or ESCAPE key is pressed
    
    window.fill(BLACK)
    #clear screen each frame
    
    dt = clock.tick(fps) / 1000
    #calculate time between frames
    
    update(dt)
    draw()
    #update and draw all objects/sprites
    
    pg.display.update()
    #show changes and restrict framerate
#game loop