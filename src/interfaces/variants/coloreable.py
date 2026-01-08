from ..base import Base
from ...types import Color

class Coloreable(Base):
    ''' Coloreable interface class. '''
    def __init__(self):
        super().__init__()
        # Set default color at initialization.
        self.set_color(self.get_default_color())


    ''' Coloreable specific methods. '''
    def set_color(self, color: Color) -> None:
        """Set the color of the object.

        Args:
            color (Color): The color to set.
        """
        self.color = color


    def get_color(self) -> Color:
        """Get the current color of the object.

        Returns:
            Color: The current color.
        """
        raise NotImplementedError("Subclasses must implement this method.")
    

    def get_default_color(self) -> Color:
        """Get coloreable default color.

        Returns:
            Color: The default color.
        """
        return Color.TRANSPARENT