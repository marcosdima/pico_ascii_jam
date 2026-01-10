from abc import abstractmethod


from ...entity import Entity
from ..layouts.grid import Grid
from ..figures.square import Square
from ..common.text import TextEntity
from ....types import Color, Anchor, Position
from ....utils import Coordinate


class Ascii(Entity):
    '''Base class for ASCII-style figures that use a grid of squares.'''
    def __init__(
        self,
        anchor: Anchor = Anchor.TOP_CENTER,
        from_anchor: Anchor = Anchor.BOTTOM_CENTER,
        sign_offset: float = 10.0,
    ):
        super().__init__()

        # Set sign anchor.
        self.sign_anchor = anchor
        self.from_anchor = from_anchor
        self.sign_offset = sign_offset

        # Set squares.
        self.squares: list[Square] = []

        # Default layout: a 5x5 grid.
        self.grid = Grid()
        rows, columns = self.get_default_dimensions()
        self.grid.set_grid_dimensions(rows=rows, columns=columns)
        self.add_child(self.grid)

        # Set ascii sign.
        self.sign = TextEntity(text=chr(self.get_unicode()), font_size=32)
        self.sign.set_color(color=Color.WHITE)
        self.add_child(self.sign)        
        
        # Hidding and showing sign on mouse events.
        self.mouse_on.add_callback(lambda: self.sign.show())
        self.mouse_exit.add_callback(lambda: self.sign.hide())
        self.sign.hide()

        # Callbacks.
        self.transform_changed.add_callback(self.__keep_grid_size)
        self.on_set_color.add_callback(lambda _: self.create_squares())

        # Create squares.
        self.create_squares()

        self.transform.rotation = 70


    def __keep_grid_size(self, prev, new):
        '''Keep the grid sized with this entity.'''
        self.grid.set_transform(size=new.size.to_tuple())

        # Calculate sign position.
        ascii_size = self.transform.size
        sign_size = self.sign.transform.size
        if self.sign_anchor == Anchor.TOP_CENTER:
            sign_pos = Position(ascii_size.x / 2 - sign_size.x / 2, -sign_size.y - self.sign_offset)
        elif self.sign_anchor == Anchor.BOTTOM_CENTER:
            sign_pos = Position(ascii_size.x / 2 - sign_size.x / 2, sign_size.y / 2 + self.sign_offset)
        elif self.sign_anchor == Anchor.CENTER_LEFT:
            sign_pos = Position(0, sign_size.y / 2 + self.sign_offset)
        elif self.sign_anchor == Anchor.CENTER_RIGHT:
            sign_pos = Position(ascii_size.x - sign_size.x, sign_size.y / 2 + self.sign_offset)

        self.sign.set_transform(position=sign_pos)
        
        
    def create_squares(self):
        '''Create square figures from a list of ((row, col), Color) items.'''
        if self.squares:
            # Clear previous squares.
            self.remove_areas(self.squares)
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
            square.disable_collide()
        self.add_areas(self.squares)


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
    