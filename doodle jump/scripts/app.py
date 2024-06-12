class App():
    def __init__(self):
        self.scene = pygame.display.set_mode((480, 720))
        self.clock = pygame.time.Clock()
        self.running = True 
        self.MaxFPS = 60

    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def render():
        self.scene.fill((0, 0, 0))
        pygame.display.update()
    
    def run():
        while self.running == True:
            self.handle_events()
            self.render()
            self.update()