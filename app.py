import pygame
import os
from scripts.game import Game

class App():
    def __init__(self):
        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock()
        self.running = True 
        self.MaxFPS = 60
        pygame.display.set_caption('Doodle Jump')
        image = pygame.image.load(os.path.join('assets', 'icons', 'icon.iso'))
        pygame.display.set_icon(image)
        self.game = Game()

    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render(self):
        self.scene.fill((0, 0, 0))
        self.game.render_object(self.scene)
        pygame.display.update()
    
    def run():
        while self.running == True:
            self.handle_events()
            self.render()
            self.update()


        