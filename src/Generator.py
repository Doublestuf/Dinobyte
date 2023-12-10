import random
#import random module for randomized number generation

from engine import window
#import engine to keep trees on screen

from src.Tree import Tree
#import the tree class for tree creation

class Generator:
    def __init__(self) -> None:
        self.generated_objects = []
        #keep track of generated trees and rocks
        
    def generate_tree(self) -> Tree:
        random_x = random.randint(0, window.get_width())
        random_y = random.randint(0, window.get_height())
        random_size = random.randint(30, 50)
        #create random numbers in a set range for the tree's position and size
        
        tree = Tree(random_x, random_y, random_size)
        #create the tree object
        
        tree.rect.clamp_ip(window.get_rect())
        #keep the tree placed on the screen
        
        return tree
        #return the tree for use in other functions
    
    def generate_trees(self, amount:int = 0) -> None:
        if not amount:
            amount = random.randint(3, 10)
        #add option to generate a random amount of trees
        
        for _ in range(amount):
            self.generated_objects.append(self.generate_tree())
        #generate a set amount of trees and add them to the list of generated objects