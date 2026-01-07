from abc import abstractmethod


from ...entity import Entity
from ..layouts.grid import Grid
from ..figures.square import Square
from ..sign import Sign, Anchor
from ....types import Color


class Ascii(Entity):
    '''Base class for ASCII-style figures that use a grid of squares.'''
    def get_default_dimensions(self) -> tuple[int, int]:
        ''' Get the default grid dimensions (rows, columns). '''
        return (5, 5)


    def create_squares(self, positions: list[tuple[tuple[int, int], Color]]):
        '''Create square figures from a list of ((row, col), Color) items.'''
        if self.squares:
            # Clear previous squares.
            for square in self.squares:
                self.grid.modules.family.remove_child(square.modules.family)

        self.squares = []

        for (r, c), color in positions:
            # Create square.
            square = Square(surface=self.surface)

            # Configure square.
            square.set_color(color=color)
            square.modules.input.add_mouse_callback(
                to='on',
                callback=lambda sq=square, ow=self: sq.set_color(color=self.color.darker())
            )
            square.modules.input.add_mouse_callback(
                to='exit',
                callback=lambda sq=square, ow=self: sq.set_color(color=self.color)
            )

            # Add to grid.
            self.grid.modules.family.add_child(square.modules.family)
            self.grid.set_position(entity_id=square.id, column=c, row=r)
            
            # Store reference.
            self.squares.append(square)


    def get_coord(self, row: int, column: int) -> tuple[tuple[int, int], Color]:
        '''Get coordinate tuple for given row and column with this entity's color.'''
        return ((row, column), self.color)
    

    def from_row(self, row: int, to_col: int, from_col: int = 0) -> list[tuple[tuple[int, int], Color]]:
        '''Get list of coordinate tuples for a given row from from_col to to_col with this entity's color.'''
        return [self.get_coord(row, c) for c in range(from_col, to_col + 1)]


    def set_sign_anchor(self, anchor: Anchor):
        '''Set the anchor point for the sign entity.'''
        if hasattr(self, 'sign'):
            self.sign.anchor = anchor


    ''' Abstract methods. '''
    @abstractmethod
    def get_unicode(self) -> int:
        ''' Get the Unicode code point for this avatar. '''
        pass


    ''' Entity overrides. '''
    def set_color(self, color: Color):
        super().set_color(color)
        for square in self.squares:
            square.set_color(color=self.color)


    ''' Lifecycle methods. '''
    def set_properties(self):
        self.squares: list[Square] = []
        super().set_properties()


    def setup(self):
        super().setup()

        # Default layout: a 5x5 grid. Subclasses can call `configure_grid`.
        self.grid = Grid(surface=self.surface)
        rows, columns = self.get_default_dimensions()
        self.grid.set_grid_dimensions(rows=rows, columns=columns)
        self.modules.family.add_child(self.grid.modules.family)

        # Set ascii sign.
        self.sign = Sign(
            surface=self.surface,
            text=chr(self.get_unicode()),
            follow=self,
            anchor=Anchor.TOP_CENTER,
        )
        self.sign.hide()
        
        self.modules.family.add_child(self.sign.modules.family)
        self.modules.input.add_mouse_callback(
            to='on',
            callback=lambda sg=self.sign: sg.show()
        )
        self.modules.input.add_mouse_callback(
            to='exit',
            callback=lambda sg=self.sign: sg.hide()
        )


    def on_transform_changed(self, prev, new):
        '''Keep the grid sized with this entity.'''
        super().on_transform_changed(prev, new)
        # Forward the new size to the grid so children layout updates.
        if hasattr(self, 'grid'):
            self.grid.set_transform(size=new.size.to_tuple())
        if hasattr(self, 'sign'):
            sign_height = 50
            self.sign.set_transform(size=(new.size.x, sign_height), position=(0, -sign_height))
