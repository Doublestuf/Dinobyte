import pygame as pg
#imports

fullscreen = False
#debug

if fullscreen:
    window = pg.display.set_mode((1280, 720), pg.FULLSCREEN)
else:
    window = pg.display.set_mode((1280, 720))
#initialization

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#constants

fps = 60
clock = pg.time.Clock()
game_objects = []
#variables