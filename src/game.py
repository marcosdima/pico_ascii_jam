import pygame


from .config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    GAME_TITLE,
    BG_COLOR,
    MAIN_SCREEN,
)
from .entities import Avatar


class Game:
    '''Main class that manages the game'''
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)

        self.__set_display()

        self.clock = pygame.time.Clock()
        self.running = True

        self.entity = Avatar(surface=self.screen)
        self.entity.modules.set_wasd(speed=200.0)
        self.entity.set_transform(
            position=(100, 100),
            size=(200, 200),
            z_index=1
        )


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
            self.entity.handle_event(event)
            if event.type == pygame.QUIT:
                self.running = False


    def draw(self):
        '''Render game content.'''
        self.screen.fill(BG_COLOR)
        self.entity.draw()
        pygame.display.flip()


    def run(self):
        '''Execute main game loop.'''
        while self.running:
            # Set delta time.
            dt = self.clock.tick(FPS) / 1000.0

            # Handle events, update and draw.
            self.handle_events()
            self.entity.update(dt)
            self.draw()

        pygame.quit()
