from ...vector2 import Vector2


class Size(Vector2):
    '''2D size helper.'''
    def __init__(self, width: float = 0.0, height: float = 0.0):
        super().__init__(width, height)
        self.width = float(width)
        self.height = float(height)


    def __str__(self):
        return f"Size(width={self.width}, height={self.height})"