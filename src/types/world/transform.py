from .size import Size
from .position import Position
from ..vector2 import Vector2

class Transform:
    def __init__(
            self,
            position: Position = Position(0, 0),
            size: Size = Size(1, 1),
            scale: Vector2 = Vector2(1, 1),
        ):
        self.position = position
        self.size = size
        self.scale = scale

    
    def get_scaled_size(self) -> Size:
        '''Get the size after applying the scale.'''
        return Size(
            self.size.width * self.scale.x,
            self.size.height * self.scale.y
        )
    

    def move(self, delta: Vector2):
        '''Move the position.'''
        self.position += delta