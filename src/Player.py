import pygame as pg
#import pygaame

from engine import window
#import window to keep player on screen

from src.Entity import Entity

class Player(Entity):
    def __init__(self, width:float, height:float, x:float, y:float) -> None:
        super().__init__(width, height, x, y)
        
        self.speed = 3
        #set player's movement speed
        
    def update(self, dt:float) -> None:
        delta_speed = self.speed * 60 * dt
        #adjust speed to be framerate-independent using delta time
        
        pressed_keys = pg.key.get_pressed()
        #find currently pressed keys
        
        movement_vector = pg.math.Vector2(0, 0)
        #create vector for player movement
        
        key_map = {pg.K_w:(0, -1), 
                   pg.K_s:(0, 1), 
                   pg.K_a:(-1, 0), 
                   pg.K_d:(1, 0)}
        #map keys WASD to each movement direction
        
        for key in key_map:
            if pressed_keys[key]:
                movement_vector += pg.math.Vector2(key_map[key])
        #add current movement directions to the player movement vector
        
        if movement_vector:
            movement_vector.normalize_ip()
        #normalize the player movement vector to prevent diagonal movement from being faster than horizontal/vertical movement
        
        self.rect.move_ip(movement_vector * delta_speed)
        #move the player with the normalized movement vector and adjusted speed
        
        self.rect.clamp_ip(window.get_rect())
        #prevent player from moving off-screen