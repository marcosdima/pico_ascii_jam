from .__base import Base
from ....types import Color
from ....utils import Event


class Coloreable(Base):
    ''' Coloreable interface class. '''
    def __init__(self):
        super().__init__()
        # Set default color at initialization.
        self.on_set_color = Event[Color]()
        self.set_color(self.get_default_color())


    ''' Coloreable specific methods. '''
    def set_color(self, color: Color) -> None:
        """Set the color of the object.

        Args:
            color (Color): The color to set.
        """
        self.color = color
        self.on_set_color(color)


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