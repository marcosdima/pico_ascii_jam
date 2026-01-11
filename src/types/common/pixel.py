from .color import Color
from ..transform.vector2 import Vector2


class Pixel:
    """Represents a pixel with coordinates and color."""
    
    def __init__(self, x: int = 0, y: int = 0, color: Color = None):
        self.x = x
        self.y = y
        self.color = color or Color.WHITE
    
    
    def __str__(self) -> str:
        """Return string representation of the pixel."""
        return f"Pixel(x={self.x}, y={self.y}, color={self.color})"
    
    
    def __repr__(self) -> str:
        """Return detailed representation of the pixel."""
        return f"Pixel({self.x}, {self.y}, Color({self.color.r}, {self.color.g}, {self.color.b}, {self.color.a}))"
    
    
    def __eq__(self, other) -> bool:
        """Check if two pixels are equal."""
        if not isinstance(other, Pixel):
            return False
        return (self.x == other.x and 
                self.y == other.y and
                self.color == other.color)
    
    
    def __ne__(self, other) -> bool:
        """Check if two pixels are not equal."""
        return not self.__eq__(other)
    
    
    def __hash__(self) -> int:
        """Return hash of the pixel."""
        return hash((self.x, self.y, self.color))
    
    
    def copy(self) -> 'Pixel':
        """Return a copy of the pixel."""
        return Pixel(self.x, self.y, self.color.copy())
    
    
    def set_position(self, x: int, y: int) -> None:
        """Set the pixel position."""
        self.x = x
        self.y = y
    
    
    def set_color(self, color: Color) -> None:
        """Set the pixel color."""
        self.color = color
    
    
    def to_tuple(self) -> tuple[tuple[int, int], tuple[int, int, int, int]]:
        """Return pixel as tuple of position and color."""
        return ((self.x, self.y), self.color.to_tuple())