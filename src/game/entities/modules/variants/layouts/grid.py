from .__layout import Layout


ROWS = 'rows'
COLUMNS = 'columns'
COORDS = 'coords'


class Grid(Layout):
    ''' Grid layout module class. '''
    def _arrange_components(self):
        rows = self.settings[ROWS]
        columns = self.settings[COLUMNS]
        owner = self.owner

        if columns == 0 or rows == 0:
            return

        cell_width = owner.size.x / columns
        cell_height = owner.size.y / rows
        
        # Small overlap to prevent gaps when rotating (1.01 = 1% larger)
        # This compensates for floating point precision and rotation artifacts
        overlap_factor = 1.1
        
        # Calculate offset to center the grid (pymunk uses center as origin)
        grid_offset_x = -owner.size.x / 2
        grid_offset_y = -owner.size.y / 2

        for component in self.components:
            col, row = self.get_coords(component.id)

            # Position relative to grid origin (top-left), then center the cell, then offset to center grid
            pos = (
                grid_offset_x + col * cell_width + cell_width / 2,
                grid_offset_y + row * cell_height + cell_height / 2,
            )
            size = (cell_width * overlap_factor, cell_height * overlap_factor)
            
            self._set_as_follower(component, pos)
            component.set_size(size)
            

    def get_coords(self, id: int) -> tuple[int, int]:
        ''' Get number of rows. '''
        return self._get_component_setting_field(id, COORDS, (0, 0))


    def _validate_settings(self, settings) -> bool:
        rows = settings.get(ROWS, None)
        columns = settings.get(COLUMNS, None)

        return isinstance(rows, int) and rows >= 0 and isinstance(columns, int) and columns >= 0
    

    def _validate_component_setting(self, component_setting: dict) -> bool:
        if COORDS in component_setting:
            coords = component_setting[COORDS]
            if (
                not isinstance(coords, tuple)
                or len(coords) != 2
                or not all(isinstance(c, int) for c in coords)
            ):
                raise ValueError("Coords must be a pair of integers.")
            return True
        return False
