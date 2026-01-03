import pygame


class Font:
    def __init__(self, font_path: str, font_size: int):
        self.size = font_size
        self.path = font_path
        self.__set_font()
        

    def __set_font(self):
        '''Set font size.'''
        try:
            self.font = pygame.font.Font(self.path, self.size)
        except (pygame.error, FileNotFoundError):
            # If font doesn't exist, use default font
            print(f'Warning: Font not found at {self.path}')
            print('Using pygame default font')
            self.font = pygame.font.Font(None, self.size)

        
    def render(self, text: str, antialias: bool, color: pygame.Color) -> pygame.Surface:
        '''Render text to a surface.'''
        return self.font.render(text, antialias, color)
    

    def set_font_size(self, font_size: int):
        '''Set font size.'''
        self.size = font_size
        self.__set_font()

