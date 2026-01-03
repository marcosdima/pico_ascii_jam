import enum


from ..vector2 import Vector2


class AnchorPosition(enum.Enum):
    TOP_LEFT = 0
    TOP_CENTER = 1
    TOP_RIGHT = 2
    CENTER_LEFT = 3
    CENTER = 4
    CENTER_RIGHT = 5
    BOTTOM_LEFT = 6
    BOTTOM_CENTER = 7
    BOTTOM_RIGHT = 8


class Anchor:
    def __init__(
            self,
            point: tuple[float, float] = (0, 0),
            position: AnchorPosition = AnchorPosition.TOP_LEFT,
        ):
        self.point = Vector2.from_tuple(point)
        self.position = position


    def copy(self) -> 'Anchor':
        '''Return a copy of the anchor.'''
        return Anchor(self.point.to_tuple(), self.position)