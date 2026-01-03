from ...types import Color

class Coloreable:
    '''Interface for objects that can have their color changed.'''
    def __init__(self):
        super().__init__()
        self.color: Color = Color(255, 255, 255)  # Default white color
        

    def set_color(self, color: Color) -> None:
        '''Set the color of the object.
        
        Args:
            color (Color): The RGB color to set.
        '''
        self.color = color


    def get_color(self) -> Color:
        '''Get the current color of the object.
        
        Returns:
            Color: The current RGB color.
        '''
        return self.color