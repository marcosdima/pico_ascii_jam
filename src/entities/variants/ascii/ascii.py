from abc import abstractmethod


from ...entity import Entity
from ..layouts.grid import Grid
from ..figures.square import Square
from ..sign import Sign, Anchor
from ....types import Color
from ....utils import Coordinate


class Ascii(Entity):
    '''Base class for ASCII-style figures that use a grid of squares.'''
    def __init__(self):
        super().__init__()

        # Set squares.
        self.squares: list[Square] = []

        # Default layout: a 5x5 grid.
        self.grid = Grid()
        rows, columns = self.get_default_dimensions()
        self.grid.set_grid_dimensions(rows=rows, columns=columns)
        self.add_child(self.grid)

        # Set ascii sign.
        self.sign = Sign(
            text=chr(self.get_unicode()),
            follow=self,
            anchor=Anchor.TOP_CENTER,
        )
        self.add_child(self.sign)
        self.sign.hide()
        self.mouse_on.add_callback(lambda: self.sign.show())
        self.mouse_exit.add_callback(lambda: self.sign.hide())

        # Callbacks.
        self.transform_changed.add_callback(self.__keep_grid_size)
        self.on_set_color.add_callback(lambda _: self.create_squares())

        # Create squares.
        self.create_squares()


    def __keep_grid_size(self, prev, new):
        '''Keep the grid sized with this entity.'''
        self.grid.set_transform(size=new.size.to_tuple())
        sign_height = 50
        self.sign.set_transform(size=(new.size.x, sign_height), position=(0, -sign_height))


    def create_squares(self):
        '''Create square figures from a list of ((row, col), Color) items.'''
        if self.squares:
            # Clear previous squares.
            for square in self.squares:
                self.grid.remove_child(square)

        self.squares = []
        for coord in self.get_square_values():
            # Get values.
            (r, c), content = coord.as_tuple()

            # Create square.
            square = Square()

            # Configure square.
            square.set_color(color=content.get('color', self.get_default_color()))

            # Add to grid.
            self.grid.add_child(square)
            self.grid.set_grid_position(square, column=c, row=r)
            
            # Store reference.
            self.squares.append(square)


    def set_sign_anchor(self, anchor: Anchor):
        '''Set the anchor point for the sign entity.'''
        if hasattr(self, 'sign'):
            self.sign.anchor = anchor


    ''' Color overrides. '''
    def get_default_color(self):
        return Color.WHITE


    ''' Abstract methods. '''
    @abstractmethod
    def get_unicode(self) -> int:
        ''' Get the Unicode code point for this avatar. '''
        pass


    @abstractmethod
    def get_default_dimensions(self) -> tuple[int, int]:
        ''' Get the default grid dimensions (rows, columns). '''
        pass


    @abstractmethod
    def get_square_values(self) -> list[Coordinate]:
        ''' Get the list of square positions and colors for this avatar. '''
        pass
    