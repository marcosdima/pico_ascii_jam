import pygame


from .config import WINDOW_WIDTH, WINDOW_HEIGHT, FPS, GAME_TITLE, BG_COLOR
from .scenes.menu import MenuScene


class Game:
    '''Main class that manages the game'''
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # Current scene
        self.current_scene = MenuScene(self)


    def handle_events(self):
        '''Handle game events.'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                self.current_scene.handle_event(event)


    def update(self, dt):
        '''Update game logic.'''
        self.current_scene.update(dt)


    def draw(self):
        '''Render game content.'''
        self.screen.fill(BG_COLOR)
        self.current_scene.draw(self.screen)
        pygame.display.flip()


    def run(self):
        '''Execute main game loop.'''
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            self.update(dt)
            self.draw()

        pygame.quit()
