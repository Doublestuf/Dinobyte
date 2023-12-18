import pygame as pg

from inventory.Item import Item

class Inventory:
    def __init__(self) -> None:
        self.items = {}
        
    def add_item(self, item:Item, amount:int) -> None:
        if item in self.items:
            self.items[item] += amount
        else:
            self.items[item] = amount
            
    def remove_item(self, item:Item, amount:int) -> None:
        if not item in self.items or self.items[item] < amount:
            return
        else:
            self.items[item] -= amount
    
    def draw_items(self, surface:pg.Surface):
        pass