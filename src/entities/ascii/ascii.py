import pygame


from ...types import Font
from ..entity import Entity, abstractmethod


class Ascii(Entity):
    ''' An entity that represents ASCII characters on the screen. '''
    def set_unicode(self, unicode_value: int):
        '''Set character from unicode code point.'''
        self.unicode = chr(unicode_value)
        if hasattr(self, 'transform'):
            self.__set_transform_from_unicode()
        return self
    

    def get_default_unicode(self) -> int:
        return 65 # Default character 'A'
    

    def __set_transform_from_unicode(self):
        surf = self.font.render(self.unicode, False, self.color.to_pygame_color())
        bbox = surf.get_bounding_rect()

        tight = pygame.Surface((bbox.width, bbox.height), pygame.SRCALPHA)
        tight.blit(surf, (0, 0), bbox)

        self.image = tight
        self.transform.set_size(bbox.width, bbox.height)


    ''' Entity overrides. '''
    def set_transform(self, position = None, size = None, scale = None):
        super().set_transform(position, size, scale)
        self.font.set_font_size(int(self.font_size * self.transform.scale.y))
        return self
    

    ''' Entity life cycle overrides. '''
    def setup(self):
        self.font_size = 16
        self.font = Font('assets/pico-8.otf', self.font_size)
        if not hasattr(self, 'unicode'):
            self.set_unicode(self.get_default_unicode())

        super().setup()

        self.__set_transform_from_unicode()

        
    def draw(self):
        super().draw()

        x, y = self.transform.position.to_tuple()
        w, h = self.transform.get_scaled_size().to_tuple()
        
        # Scale image to match transform scale
        scaled_image = pygame.transform.scale(self.image, (int(w), int(h)))
        self.surface.blit(scaled_image, (int(x), int(y)))

