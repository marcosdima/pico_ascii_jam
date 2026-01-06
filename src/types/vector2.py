class Vector2:
    '''2D vector with basic helpers.'''

    ZERO: 'Vector2' = None
    ONE: 'Vector2' = None
    RIGHT: 'Vector2' = None
    LEFT: 'Vector2' = None
    UP: 'Vector2' = None
    DOWN: 'Vector2' = None

    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)


    def to_tuple(self) -> tuple[float, float]:
        '''Return vector as tuple.'''
        return (self.x, self.y)
    

    def copy(self) -> 'Vector2':
        '''Return a copy of the vector.'''
        return Vector2(self.x, self.y)
    

    def normalized(self) -> 'Vector2':
        '''Return a normalized version of the vector.'''
        length = (self.x ** 2 + self.y ** 2) ** 0.5
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)
    

    def is_zero(self) -> bool:
        '''Check if the vector is zero.'''
        return self.x == 0.0 and self.y == 0.0
    

    def absolute(self) -> 'Vector2':
        '''Return a vector with absolute values.'''
        return Vector2(abs(self.x), abs(self.y))
    

    def is_positive(self) -> bool:
        '''Check if both components are positive.'''
        return self.x >= 0.0 and self.y >= 0.0


    @classmethod
    def from_tuple(cls, values: tuple) -> 'Vector2':
        '''Create Vector2 from tuple (x, y).'''
        if len(values) != 2:
            raise ValueError('Tuple must have length 2')
        return cls(values[0], values[1])


    @classmethod
    def from_list(cls, values: list) -> 'Vector2':
        '''Create Vector2 from list [x, y].'''
        if len(values) < 2:
            raise ValueError('List must have at least length 2')
        return cls(values[0], values[1])


    @classmethod
    def from_iterable(cls, iterable) -> 'Vector2':
        '''Create Vector2 from any iterable of length 2.'''
        vals = list(iterable)
        if len(vals) < 2:
            raise ValueError('Iterable must have at least length 2')
        return cls(vals[0], vals[1])
    

    def __add__(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        return Vector2(self.x + other.x, self.y + other.y)
    
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector2(self.x * other, self.y * other)
        if isinstance(other, Vector2):
            return Vector2(self.x * other.x, self.y * other.y)
        return NotImplemented
    
    
    def __rmul__(self, other):
        return self.__mul__(other)
    

    def __sub__(self, other):
        if not isinstance(other, Vector2):
            return NotImplemented
        return Vector2(self.x - other.x, self.y - other.y)
    

    def __truediv__(self, scalar: float):
        return Vector2(self.x / scalar, self.y / scalar)
    

    def __iter__(self):
        yield self.x
        yield self.y


    def __str__(self):
        return f'Vector2({self.x}, {self.y})'


# Initialize constant.
Vector2.ONE = Vector2(1.0, 1.0)
Vector2.RIGHT = Vector2(1.0, 0.0)
Vector2.LEFT = Vector2(-1.0, 0.0)
Vector2.UP = Vector2(0.0, -1.0)
Vector2.DOWN = Vector2(0.0, 1.0)
