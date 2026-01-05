import pygame


from .size import Size
from .position import Position
from ..vector2 import Vector2


class Transform:
    def __init__(
            self,
            position: Position = Position(0, 0),
            size: Size = Size(1, 1),
            scale: Vector2 = Vector2(1, 1),
            z_index: int = 0,
        ):
        self.position = position
        self.size = size
        self.scale = scale
        self.z_index = z_index


    def set_size(self, width: int, height: int):
        '''Set the size.'''
        self.size = Size(width, height)


    def set_scale(self, scale_x: float, scale_y: float):
        '''Set the scale.'''
        self.scale = Vector2(scale_x, scale_y)


    def set_position(self, x: float, y: float):
        '''Set the position.'''
        self.position = Position(x, y)


    def set_z_index(self, z_index: int):
        '''Set the z-index.'''
        self.z_index = z_index


    def get_scaled_size(self) -> Size:
        '''Get the size after applying the scale.'''
        return Size(
            self.size.width * self.scale.x,
            self.size.height * self.scale.y
        )
    

    def get_rect(self) -> pygame.Rect:
        '''Get the pygame.Rect representing the transform.'''
        real_size = self.get_scaled_size()
        return pygame.Rect(
            int(self.position.x),
            int(self.position.y),
            int(real_size.width),
            int(real_size.height)
        )   
    
    
    def copy(self) -> 'Transform':
        '''Create a copy of the transform.'''
        return Transform(
            position=Position(self.position.x, self.position.y),
            size=Size(self.size.width, self.size.height),
            scale=Vector2(self.scale.x, self.scale.y),
            z_index=self.z_index
        )
    

    def __str__(self):
        return f'Transform(position={self.position}, size={self.size}, scale={self.scale}, z_index={self.z_index})'
