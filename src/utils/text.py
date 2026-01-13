import pygame


from ..types import Color, Font
from config import FONT_PATH


class Text:
    '''Text renderer with automatic case swap and rendering capabilities.
    
    This class combines the automatic case swap (useful for inverted fonts like pico-8)
    with full text rendering and drawing support.
    '''
    
    def __init__(self, text: str, font_size: int = 16, color: Color = None):
        '''Initialize Text with content, size, and optional color.
        
        Args:
            text (str): The text to render (will be swapped case).
            font_size (int): Font size in pixels.
            color (Color): Text color. Defaults to white.
        '''
        self.value = text.swapcase()
        self.font_size = font_size
        self.color = color if color else Color.WHITE
        self.font = Font(FONT_PATH, font_size)
        self.rendered_surface = None
        self.__render()
    
    
    def __render(self):
        """Render the text to a surface."""
        self.rendered_surface = self.font.render(
            self.value,
            True,  # antialias
            self.color.to_pygame_color()
        )
    
    
    def set_text(self, text: str):
        """Update text content (case will be swapped) and re-render."""
        self.value = text.swapcase()
        self.__render()
    
    
    def set_color(self, color: Color):
        """Update text color and re-render."""
        self.color = color
        self.__render()
    
    
    def set_font_size(self, size: int):
        """Update font size and re-render."""
        self.font_size = size
        self.font.set_font_size(size)
        self.__render()
    
    
    def draw(self, surface: pygame.Surface, position: tuple[int, int]):
        """Draw the text at the given position on the surface."""
        if self.rendered_surface:
            surface.blit(self.rendered_surface, position)
    
    
    def get_size(self) -> tuple[int, int]:
        """Get the size of the rendered text."""
        if self.rendered_surface:
            return self.rendered_surface.get_size()
        return (0, 0)
    
    
    def __str__(self) -> str:
        '''Return the swapped-case text as a string.'''
        return self.value
    
    
    def __repr__(self) -> str:
        '''Return the representation of the swapped-case text.'''
        return self.value

