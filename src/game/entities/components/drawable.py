from .__base import Base, pygame
from ....types import Color


class Drawable(Base):
    ''' Drawable interface. '''
    def draw_rect(self, rect: pygame.Rect, color: Color):
        local = pygame.Surface(rect.size, pygame.SRCALPHA)
        pygame.draw.rect(local, color.to_pygame_color(), local.get_rect())

        transformed = self.get_transformed_surface(local)

        draw_rect = transformed.get_rect(center=rect.center)
        self.base_surface.blit(transformed, draw_rect)


        