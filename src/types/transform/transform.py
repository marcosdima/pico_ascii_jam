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


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Transform):
            return NotImplemented
        return (
            self.position == other.position and
            self.size == other.size and
            self.scale == other.scale and
            self.z_index == other.z_index
        )   