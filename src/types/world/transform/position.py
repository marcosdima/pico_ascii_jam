from ...vector2 import Vector2


class Position(Vector2):
    '''2D position helper.'''
    def direction_to(self, other: 'Position') -> 'Vector2':
        '''Return direction vector from this position to another.'''
        return Vector2(other.x - self.x, other.y - self.y)
    

    def copy(self):
        return Position(self.x, self.y)


    ''' Python special methods. '''
    def __str__(self):
        return f"Position(x={self.x}, y={self.y})"
