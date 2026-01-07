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


class Game:
    '''Main class that manages the game'''
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.__set_display()

        self.clock = pygame.time.Clock()
        self.running = True

        self.player = Player(surface=self.screen)
        
        # Initialize UI
        self.ui_elements: list[UI] = []
        self.status_ui = Status(surface=self.screen)
        self.status_ui.set_resources(self.player.resources)
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
            self.player.entity.handle_event(event)
            if event.type == pygame.QUIT:
                self.running = False


    def draw(self):
        '''Render game content.'''
        self.screen.fill(BG_COLOR)
        
        # Draw entities first
        self.player.entity.draw()
        
        # Draw UI on top (always visible)
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
            self.player.entity.update(dt)
            
            # Update UI elements
            for ui_element in self.ui_elements:
                ui_element.update(dt)
            
            self.draw()

        pygame.quit()
