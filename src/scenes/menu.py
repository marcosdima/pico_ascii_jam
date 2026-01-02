import pygame


from ..config import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_COLOR, FONT_PATH
from ..types import Text


class MenuScene:
    '''Main menu scene that displays "Hello World"'''
    def __init__(self, game):
        self.game = game
        self.font_size = 72
        try:
            self.font = pygame.font.Font(FONT_PATH, self.font_size)
        except (pygame.error, FileNotFoundError):
            # If font doesn't exist, use default font
            print(f'Warning: Font not found at {FONT_PATH}')
            print('Using pygame default font')
            self.font = pygame.font.Font(None, self.font_size)

        self.text = Text('Hello World!')
        self.text_surface = self.font.render(self.text, False, TEXT_COLOR)


    def handle_event(self, event):
        '''Handle input events.'''
        pass


    def update(self, dt):
        '''Update scene logic.'''
        pass


    def draw(self, screen):
        '''Render the scene to the screen.'''
        # Calculate centered position
        text_rect = self.text_surface.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        # Draw the text
        screen.blit(self.text_surface, text_rect)
