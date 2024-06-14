import pygame
from scripts.sprite import Sprite 

class Player(Sprite):
    def  __init__(self, coords, image, speed, jump_power, gravity):
        super().__init__(coords, image):
        
        self.jump_power = jump_power
        self.speed = speed
        self.gravity = gravity
        self.is_walking_right = False
        self.is_walking_left = False