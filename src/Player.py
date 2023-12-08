import pygame as pg
#import pygaame

from engine import window
#import window to keep player on screen

class Player:
    def __init__(self, width:float, height:float, x:float, y:float) -> None:
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = (x, y)
        #set player rect's size and location
        
        self.speed = 3
        #set player's movement speed
        
    def update(self) -> None:
        pressed_keys = pg.key.get_pressed()
        key_map = {pg.K_w:(0, -self.speed), 
                   pg.K_s:(0, self.speed), 
                   pg.K_a:(-self.speed, 0), 
                   pg.K_d:(self.speed, 0)}
        #map keys WASD to each movement direction
        
        for key in key_map:
            if pressed_keys[key]:
                self.rect.move_ip(key_map[key])
        #move player according to the key map
        
        self.rect.clamp_ip(window.get_rect())
        #prevent player from moving off-screen
    
    def draw(self, surface:pg.Surface, color:pg.Color) -> None:
        pg.draw.rect(surface, color, self.rect)
        #draw player rect to designated surface