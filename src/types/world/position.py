from typing import TYPE_CHECKING


from ..vector2 import Vector2


if TYPE_CHECKING:
    from ...models import Model


class Position(Vector2):
    '''2D position helper.'''

    def relative_to(self, other: 'Model') -> 'Position':
        '''Return absolute position relative to a model's position.'''
        return Position(self.x + other.position.x, self.y + other.position.y)
    

    def direction_to(self, other: 'Position') -> 'Vector2':
        '''Return direction vector from this position to another.'''
        return Vector2(other.x - self.x, other.y - self.y)
    

    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"
