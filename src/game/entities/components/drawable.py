import math


from .__base import Base, pygame
from ....types import Color


class Drawable(Base):
    ''' Drawable interface. '''
    def draw_rect(self, color: Color):
        local = pygame.Surface(self.size, pygame.SRCALPHA)
        pygame.draw.rect(local, color.to_pygame_color(), local.get_rect())

        rotated = pygame.transform.rotate(
            local,
            -math.degrees(self.body.angle)
        )

        rect = rotated.get_rect(center=self.body.position)
        self.base_surface.blit(rotated, rect)


        