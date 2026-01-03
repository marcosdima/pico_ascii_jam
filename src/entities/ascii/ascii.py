import pygame
from ...types import Font
from ..entity import Entity


class Ascii(Entity):
    ''' An entity that represents ASCII characters on the screen. '''
    def set_unicode(self, unicode_value: int):
        '''Set character from unicode code point.'''
        self.unicode = chr(unicode_value)
        return self
    

    ''' Entity overrides. '''
    def set_transform(self, position = None, size = None, scale = None):
        super().set_transform(position, size, scale)
        self.font.set_font_size(int(self.font_size * self.transform.scale.y))
        return self
    

    ''' Entity life cycle overrides. '''
    def setup(self):
        self.font_size = 16
        self.font = Font('assets/pico-8.otf', self.font_size)
        self.set_unicode(65)  # Default character 'A'

        super().setup()

        self.transform.set_size(*self.font.font.size(self.unicode))

        
    def draw(self):
        super().draw()

        # Render the ASCII character to surface at the entity's position
        x, y = self.get_global_position().to_tuple()
        color = self.get_color().to_pygame_color()
        
        text_surface = self.font.render(self.unicode, False, color)
        self.surface.blit(text_surface, (int(x), int(y)))

