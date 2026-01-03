class Vector2:
    '''2D vector with basic helpers.'''
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = float(x)
        self.y = float(y)


    def to_tuple(self) -> tuple[float, float]:
        '''Return vector as tuple.'''
        return (self.x, self.y)
    

    def copy(self) -> 'Vector2':
        '''Return a copy of the vector.'''
        return Vector2(self.x, self.y)


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
