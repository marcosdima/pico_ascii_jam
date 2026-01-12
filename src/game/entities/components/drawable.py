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
        self.base_surface.blit(rotated, rect)


    def draw_shape(self, shape: pymunk.Shape, color: Color):
        ''' Draw shape using physics vertices (follows movement accurately). '''
        if isinstance(shape, pymunk.Poly):
            # Get vertices in world space
            vertices = [self.body.local_to_world(v) for v in shape.get_vertices()]
            # Convert to tuples for pygame
            vertices_tuple = [(v.x, v.y) for v in vertices]
            
            if len(vertices_tuple) > 2:
                pygame.draw.polygon(self.base_surface, color.to_pygame_color(), vertices_tuple)


        