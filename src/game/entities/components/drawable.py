import math, pymunk


from .__base import Base, pygame
from ....types import Color


class Drawable(Base):
    ''' Drawable interface. '''
    def draw_rect(self, size: tuple[float, float], color: Color, offset: pymunk.Vec2d = pymunk.Vec2d(0, 0)):
        ''' Draw a rectangle shape. '''
        local = pygame.Surface(size, pygame.SRCALPHA)
        pygame.draw.rect(local, color.to_pygame_color(), local.get_rect())

        rotated = pygame.transform.rotate(
            local,
            -math.degrees(self.body.angle)
        )

        rotated_offset = offset.rotated(-self.body.angle)
        world_pos = pymunk.Vec2d(*self.body.position) + rotated_offset

        rect = rotated.get_rect(center=world_pos)
        print(f"[Drawable] draw_rect id={self.id} size={size} color={color} body_pos={self.body.position} angle={math.degrees(self.body.angle):.1f} world_pos={world_pos}")
        self.base_surface.blit(rotated, rect)


        