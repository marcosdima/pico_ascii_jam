import pygame


from ...entity import Entity
from ....types import Text, Font, Size
from ....config import FONT_PATH


class TextEntity(Entity):
    def __init__(self, text: str, font_size: int = 12):
        super().__init__()
        self.text = Text(text=text)
        self.font_size = font_size
        self.__set_font()
        self.draw.add_callback(self.__on_draw)
        self.on_set_color.add_callback(lambda _: self.__set_font())


    def __on_draw(self):
        if not self.rendered_surface:
            return
        pos = self.get_global_position()
        self.surface.blit(self.rendered_surface, (pos.x, pos.y))


    def __set_font(self):
        self.font = Font(font_path=FONT_PATH, font_size=self.font_size)

        rendered = self.font.render(
            str(self.text),
            True,
            self.color.to_pygame_color()
        )
        self.rendered_surface = self.__trim_surface(rendered)
        self.rendered_size = (
            self.rendered_surface.get_width(),
            self.rendered_surface.get_height()
        )
        self.set_transform(size=Size(*self.rendered_size))


    def __trim_surface(self, surface: pygame.Surface) -> pygame.Surface:
        '''Trim whitespace from a surface.
        
        Args:
            surface: The surface to trim.
            
        Returns:
            The trimmed surface.
        '''
        # Get the bounding rect of non-transparent pixels
        mask = pygame.mask.from_surface(surface)
        rect = mask.get_bounding_rects()
        
        if not rect:
            return surface
        
        # Get the union of all bounding rects
        bounding_rect = rect[0]
        for r in rect[1:]:
            bounding_rect = bounding_rect.union(r)
        
        # Create a new surface with just the visible content
        trimmed = surface.subsurface(bounding_rect).copy()
        return trimmed
    

    def modify_text(self, new_text: str):
        ''' Modify the text displayed by the entity.'''
        self.text = Text(text=new_text)
        self.__set_font()
        