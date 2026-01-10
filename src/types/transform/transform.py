from .size import Size
from .position import Position


class Transform:
    def __init__(
            self,
            position: Position = Position(0, 0),
            size: Size = Size(1, 1),
            scale: float = 0.0,
            rotation: float = 0.0,
            z_index: int = 0,
        ):
        self.position = position
        self.size = size
        self.scale = scale
        self.z_index = z_index
        self.rotation = rotation


    def copy(self) -> 'Transform':
        '''Create a copy of the transform.'''
        return Transform(
            position=Position(self.position.x, self.position.y),
            size=Size(self.size.width, self.size.height),
            scale=self.scale,
            rotation=self.rotation,
            z_index=self.z_index
        )
    

    def __str__(self):
        return f'Transform(p={self.position}, s={self.size}, sc={self.scale}, rot={self.rotation}, z={self.z_index})'


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Transform):
            return NotImplemented
        return (
            self.position == other.position and
            self.size == other.size and
            self.scale == other.scale and
            self.rotation == other.rotation and
            self.z_index == other.z_index
        )   