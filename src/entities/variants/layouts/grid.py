from ...entity import Entity


class Grid(Entity):
    ''' Grid entity class. '''
    def get_cell_size(self) -> tuple[float, float]:
        if self.columns == 0 or self.rows == 0:
            return (0.0, 0.0)
        
        size = self.get_size()
        return (size.x / self.columns, size.y / self.rows)
    

    def set_grid_dimensions(self, rows: int = None, columns: int = None):
        self.columns = columns if columns is not None else self.columns
        self.rows = rows if rows is not None else self.rows


    def set_position(self, entity_id: int, column: int, row: int):
        self.positions[entity_id] = (column, row)


    ''' Lifecycle methods. '''
    def setup(self):
        super().setup()

        # Set default grid values.
        self.columns = 2
        self.rows = 2
        self.positions: dict[int, tuple[int, int]] = {}
        self.modules.set_debug()

    
    def update(self, delta_time):
        super().update(delta_time)
        
        for child in self.modules.family.get_children():
            owner = child.owner

            current = self.positions.get(owner.id, (0, 0))
            cell_width, cell_height = self.get_cell_size()

            # Desired position and size in world space (after parent's scale)
            world_pos = (
                current[0] * cell_width,
                current[1] * cell_height,
            )
            world_size = (cell_width, cell_height)

            # Compute owner's total scale (including parent's scale) and
            # convert world-space values to local values so that after
            # scaling the entity fills the cell exactly.
            owner_scale = owner.get_scale()

            # Guard against zero scale to avoid division by zero.
            sx = owner_scale.x if owner_scale.x != 0 else 1.0
            sy = owner_scale.y if owner_scale.y != 0 else 1.0

            local_pos = (world_pos[0] / sx, world_pos[1] / sy)
            local_size = (world_size[0] / sx, world_size[1] / sy)

            owner.set_transform(
                position=local_pos,
                size=local_size
            )
            self.positions[owner.id] = current