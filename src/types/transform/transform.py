from typing import Optional

from .position import Position
from .size import Size


class Transform:
    def __init__(
        self,
        position: Optional[Position] = None,
        size: Optional[Size] = None,
        scale: float = 1.0,
        rotation: float = 0.0,
        z_index: int = 0,
    ):
        self.position = position.copy() if position is not None else Position()
        self.size = size.copy() if size is not None else Size(1.0, 1.0)
        self.scale = scale
        self.z_index = z_index
        self.rotation = rotation


    def copy(self) -> 'Transform':
        return Transform(
            position=self.position.copy(),
            size=self.size.copy(),
            scale=self.scale,
            rotation=self.rotation,
            z_index=self.z_index,
        )


    def __str__(self):
        return f'Transform(p={self.position}, s={self.size}, sc={self.scale}, rot={self.rotation}, z={self.z_index})'


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Transform):
            return NotImplemented
        return (
            self.position == other.position
            and self.size == other.size
            and self.scale == other.scale
            and self.rotation == other.rotation
            and self.z_index == other.z_index
        )


    def __add__(self, other: object) -> 'Transform':
        if not isinstance(other, Transform):
            return NotImplemented
        return Transform(
            position=self.position + other.position,
            size=self.size.copy(),# + other.size,
            scale=self.scale * other.scale,
            rotation=self.rotation + other.rotation,
            z_index=self.z_index + other.z_index,
        )


    def __sub__(self, other: object) -> 'Transform':
        if not isinstance(other, Transform):
            return NotImplemented
        return Transform(
            position=self.position - other.position,
            size=self.size.copy(),# - other.size,
            scale=self.scale / other.scale,
            rotation=self.rotation - other.rotation,
            z_index=self.z_index - other.z_index,
        )


    def __iadd__(self, other: object) -> 'Transform':
        result = self + other
        self.position = result.position
        # self.size = result.size
        self.scale = result.scale
        self.rotation = result.rotation
        self.z_index = result.z_index
        return self


    def __isub__(self, other: object) -> 'Transform':
        result = self - other
        self.position = result.position
        # self.size = result.size
        self.scale = result.scale
        self.rotation = result.rotation
        self.z_index = result.z_index
        return self
