from ...entity import Entity


class Grid(Entity):
    ''' Grid entity class. '''
    def __init__(self):
        self.columns = 1
        self.rows = 1
        self.positions: dict[int, tuple[int, int]] = {}
        super().__init__()
        self.update.add_callback(self.__handle_update)


    def __handle_update(self, _):
        for child in self.get_children():
            current = self.positions.get(child.id, (0, 0))
            cell_width, cell_height = self.get_cell_size()

            # Desired position and size in world space (after parent's scale)
            pos = (
                current[0] * cell_width,
                current[1] * cell_height,
            )
            size = (cell_width, cell_height)


            child.set_transform(
                position=pos,
                size=size
            )
            self.positions[self.id] = current


    def get_cell_size(self) -> tuple[float, float]:
        if self.columns == 0 or self.rows == 0:
            return (0.0, 0.0)
        
        size = self.get_size()
        return (size.x / self.columns, size.y / self.rows)
    

    def set_grid_dimensions(self, rows: int = None, columns: int = None):
        self.columns = columns if columns is not None else self.columns
        self.rows = rows if rows is not None else self.rows


    def set_grid_position(self, entity: Entity, column: int, row: int):
        self.positions[entity.id] = (column, row)