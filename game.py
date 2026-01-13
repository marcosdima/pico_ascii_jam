import pygame
import pymunk
import pymunk.pygame_util

from config import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    GAME_TITLE,
    BG_COLOR,
    MAIN_SCREEN,
)
from src.game.scenes.menu import Menu
from src.game.entities import Player, GLOBAL


class Game:
    ''' Game handler class (pygame + pymunk template)'''

    def __init__(self):
        # -------- pygame --------
        pygame.init()

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT),
            display=MAIN_SCREEN
        )
        pygame.display.set_caption(GAME_TITLE)

        self.clock = pygame.time.Clock()
        self.running = True

        # -------- pymunk --------
        self.space = pymunk.Space()
        #self.space.gravity = (0, 900)

        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)

        #------- game state --------
        GLOBAL.set_space(self.space)
        self.main_scene = Menu(self)
        
        # Player instance
        self.player = Player()
        self.player.body.position = (WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4)
        self.player.set_space(self.space)
        self.player.main_tool.modules.set_background()


    def handle_events(self):
        for event in pygame.event.get():
            self.main_scene.handle_event(event)
            self.player.call_handle_event(event)
            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False


    def update(self, dt: float):
        self.space.step(dt)
        GLOBAL.call_update(dt)
        self.main_scene.update(dt)
        self.player.call_update(dt)


    def draw(self):
        self.screen.fill(BG_COLOR)
        GLOBAL.call_draw(self.screen)
        self.main_scene.draw(self.screen)
        self.player.call_draw(self.screen)
        pygame.display.flip()


    def run(self):
        while self.running:
            dt = self.clock.tick(FPS) / 1000.0
            self.handle_events()
            GLOBAL.call_update(dt)
            self.update(dt)
            self.draw()

        pygame.quit()
