import pygame 
import os
from scripts.functions import load_image

class Game():
    def __init__(self):
        self.background = load_image('assets', 'images', 'background.png')
        
    def render_object(self, scene):
        scene.blit(self.background, (0, 0))