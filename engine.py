import pygame as pg
#import pygame

pg.font.init()
#initialize pygame fonts

fullscreen = False
#debug variables

if fullscreen:
    window = pg.display.set_mode((1280, 720), pg.FULLSCREEN)
else:
    window = pg.display.set_mode((1280, 720))
#create game window and set in fullscreen if setting is enabled

pg.display.set_caption("Dinobyte")
#set the title of the game window

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
#color variables

fps = 60
clock = pg.time.Clock()
game_objects = []
#variables

default_font_name = "assets/pixel_font.ttf"
#default font variable