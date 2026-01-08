import pygame


from ..entity import Entity
from ...types import Text, Font, Size, Anchor
from ...config import FONT_PATH


class Sign(Entity):
    '''Entity that displays text on screen.'''
    
    def __init__(
            self,
            surface: pygame.Surface,
            text: str,
            follow: 'Entity',
            anchor: Anchor = Anchor.CENTER,
            offset: float = 10.0,
        ):
        '''Initialize Sign entity.
        
        Args:
            surface: The pygame surface to draw on.
            text: The text to display.
        '''
        self.text_content = Text(text)
        self.font = None
        self.rendered_surface = None
        self.follow = follow    
        self.anchor = anchor
        self.offset = offset

        super().__init__(surface)
    

    def set_text(self, text: str):
        '''Set the text to display.
        
        Args:
            text: The new text to display.
        '''
        self.text_content = Text(text)


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


    def __update_rendered_surface(self, size: Size = Size(0, 0)):
        '''Update the rendered text surface.'''
        font_size = max(8, int(size.y / 2))

        # Create or update font with new size
        self.font = Font(font_path=FONT_PATH, font_size=font_size)
        
        # Render text
        rendered = self.font.render(
            str(self.text_content),
            True,
            self.color.to_pygame_color()
        )
        
        # Trim whitespace
        self.rendered_surface = self.__trim_surface(rendered)


    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()
        self.__update_rendered_surface(size=self.transform.size)


    def on_transform_changed(self, prev, new):
        '''Recalculate font size when transform changes.'''
        super().on_transform_changed(prev, new)
        self.__update_rendered_surface(size=new.size)


    def on_draw(self):
        '''Draw the text on screen.'''
        super().on_draw()

        if not self.rendered_surface:
            return
        
        # Calculate drawing position
        follow_rect = self.follow.get_rect()
        fx, fy, fwidth, fheight = follow_rect

        if self.anchor == Anchor.TOP_CENTER:
            draw_pos = (
                fx + (fwidth - self.rendered_surface.get_width()) / 2,
                fy - self.rendered_surface.get_height() - self.offset
            )
        elif self.anchor == Anchor.BOTTOM_CENTER:
            draw_pos = (
                fx + (fwidth - self.rendered_surface.get_width()) / 2,
                fy + fheight
            )
        elif self.anchor == Anchor.CENTER:
            draw_pos = (
                fx + (fwidth - self.rendered_surface.get_width()) / 2,
                fy + (fheight - self.rendered_surface.get_height()) / 2
            )
        elif self.anchor == Anchor.CENTER_RIGHT:
            draw_pos = (
                fx + fwidth + self.offset,
                fy + (fheight - self.rendered_surface.get_height()) / 2
            )
        else:
            draw_pos = (fx, fy)
        
        # Draw the text surface
        self.surface.blit(self.rendered_surface, draw_pos)
