import pygame


from ...config import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_COLOR, FONT_PATH
from .__scene import Scene
from ...entities import Ascii, Avatar
from ...core.parasites import WASD, Border

class MenuScene(Scene):
    '''Main menu scene that displays "Hello World"'''


    ''' Scene abstract methods. '''
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print('click en', x, y)

    
    def cleanup(self):
        pass


    def load_resources(self):
        # Avatar.
        avatar = Avatar(surface=self.game.screen)
        avatar.set_transform(scale=(8, 8), position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        avatar.add_parasite(WASD(400))
        #avatar.add_parasite(Border())

        return [
            avatar,
        ]
        