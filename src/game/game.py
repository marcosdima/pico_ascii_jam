import pygame


from ..config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    GAME_TITLE,
    BG_COLOR,
    MAIN_SCREEN,
)
from .player import Player
from .ui import Status, UI
from .scenes import Menu, Scene


class Game:
    '''Main class that manages the game'''
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.__set_display()

        self.clock = pygame.time.Clock()
        self.running = True

        # Main scene.
        self.menu: Menu = Menu()
        self.scenes: list[Scene] = [self.menu]
        self.main_scene: Scene = self.menu

        # Set player.
        self.player = Player()

        # Initialize UI
        self.ui_elements: list[UI] = []
        self.status_ui = Status(surface=self.screen)
        self.ui_elements.append(self.status_ui)


    def __set_display(self):
        '''Set the display to the specified monitor.'''
        display = pygame.display
        self.screen = display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            display=MAIN_SCREEN
        )
        display.set_caption(GAME_TITLE)


    def handle_events(self):
        '''Handle game events.'''
        for event in pygame.event.get():
            self.main_scene.main_entity.handle_event(event)
            self.player.handle_event(event)
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                key = event.key
                if key == pygame.K_ESCAPE:
                    self.running = False
                elif key == pygame.K_SPACE:
                   self.player.set_transform(scale=self.player.get_scale() * 1.1)


    def draw(self):
        '''Render game content.'''
        self.screen.fill(BG_COLOR)
        self.main_scene.main_entity.draw(self.screen)
        self.player.draw(self.screen)
        for ui_element in self.ui_elements:
            ui_element.draw()
        pygame.display.flip()


    def run(self):
        '''Execute main game loop.'''
        while self.running:
            # Set delta time.
            dt = self.clock.tick(FPS) / 1000.0

            # Handle events, update and draw.
            self.handle_events()
            self.main_scene.main_entity.update(dt)
            self.player.update(dt)
            self.status_ui.set_resources(self.player.resources)
            self.draw()

        pygame.quit()
