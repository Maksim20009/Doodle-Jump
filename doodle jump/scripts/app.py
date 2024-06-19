import pygame
import os
from scripts.game import Game
from scripts.functions import load_image


class App():
    def __init__(self):
        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock()
        self.running = True 
        self.MaxFPS = 60
        pygame.display.set_caption('Doodle Jump')
        load_image('assets', 'images', 'background.png')
        self.game = Game()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                    self.game.process_key_down_event(event.key)
            elif event.type == pygame.KEYUP:
                    self.game.process_key_up_event(event.key)

    def render(self):
        self.scene.fill((0, 0, 0))
        self.game.render_object(self.scene)
        pygame.display.update()
    
    def update(self):
        self.game.update_objects()
    
    def run(self):
        while self.running == True:
            self.handle_events()
            self.render()
            self.update()
            self.clock.tick(self.MaxFPS)