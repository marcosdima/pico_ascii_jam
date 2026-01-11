from .__layout import Layout


ROWS = 'rows'
COLUMNS = 'columns'


class Grid(Layout):
    ''' Grid layout module class. '''
    def arrange_children(self):
        rows = self.settings[ROWS]
        columns = self.settings[COLUMNS]
        owner = self.owner

        if columns == 0 or rows == 0:
            return

        cell_width = owner.size.x / columns
        cell_height = owner.size.y / rows

        for index, child in enumerate(owner.get_children()):
            col = index % columns
            row = index // columns

            pos = (
                col * cell_width,
                row * cell_height,
            )
            size = (cell_width, cell_height)

            if not owner.space:
                return
            
            owner.move_child(
                child,
                position=pos,
            )

            child.set_size(size)


    def validate_settings(self, settings) -> bool:
        rows = settings.get(ROWS, None)
        columns = settings.get(COLUMNS, None)

        return isinstance(rows, int) and rows >= 0 and isinstance(columns, int) and columns >= 0