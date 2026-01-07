from abc import abstractmethod


from ...entity import Entity
from ..layouts.grid import Grid
from ..figures.square import Square
from ....types import Color


class Ascii(Entity):
    '''Base class for ASCII-style figures that use a grid of squares.'''
    def get_default_dimensions(self) -> tuple[int, int]:
        ''' Get the default grid dimensions (rows, columns). '''
        return (5, 5)


    def create_squares(self, positions: list[tuple[tuple[int, int], Color]]):
        '''Create square figures from a list of ((row, col), Color) items.'''
        if self.squares:
            return  # Squares already created.

        self.squares = []

        for (r, c), color in positions:
            square = Square(surface=self.surface)
            self.grid.modules.family.add_child(square.modules.family)
            self.grid.set_position(entity_id=square.id, column=c, row=r)
            square.set_color(color=color)
            self.squares.append(square)


    ''' Abstract methods. '''
    @abstractmethod
    def get_unicode() -> int:
        ''' Get the Unicode code point for this avatar. '''
        pass


    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()

        # Default layout: a 5x5 grid. Subclasses can call `configure_grid`.
        self.grid = Grid(surface=self.surface)
        rows, columns = self.get_default_dimensions()
        self.grid.set_grid_dimensions(rows=rows, columns=columns)
        self.modules.family.add_child(self.grid.modules.family)

        # Container for created square figures.
        self.squares: list[Square] = []


    def on_transform_changed(self, prev, new):
        '''Keep the grid sized with this entity.'''
        super().on_transform_changed(prev, new)
        # Forward the new size to the grid so children layout updates.
        if hasattr(self, 'grid'):
            self.grid.set_transform(size=new.size.to_tuple())
