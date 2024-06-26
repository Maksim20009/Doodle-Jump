import pygame
from scripts.functions import load_image
from random import randint
from scripts.constants import display_size
from scripts.sprite import Sprite

class PlatformGenerator:
    def __init__(self, step):
        self.step = step

    def create_start_configuration(self):
        ...

    def create_platform(self, center_y):
        image = load_image('assets', 'images', 'platform.png')
        width = image.get_width()
        center_x = randint(width // 2, display_size[0] - width // 2)
        platform = Sprite(image, [center_x, center_y])

    def update(self):
        ...