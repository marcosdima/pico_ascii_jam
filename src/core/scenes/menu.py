import pygame


from ...config import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_COLOR, FONT_PATH
from .__scene import Scene
from ...entities import Ascii, Avatar
from ...core.parasites import Border, Follow

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
        ascii = Ascii(surface=self.game.screen)
        ascii.set_unicode(0x30E6)  # Unicode character 'ユ'
        ascii.set_transform(scale=(7, 7))
        #ascii.add_parasite(Border())

        # Avatar.
        avatar = Avatar(surface=self.game.screen)
        avatar.set_transform(scale=(8, 8), position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        #avatar.add_parasite(Border())
        avatar.add_follower(ascii)

        return [
            ascii,
            avatar,
        ]
        