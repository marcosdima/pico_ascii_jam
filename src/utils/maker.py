
class Coordinate:
    def __init__(self, row: int, column: int, content: object):
        self.row = row
        self.column = column
        self.content = content

    
    def as_tuple(self) -> tuple[tuple[int, int], object]:
        return ((self.row, self.column), self.content)


def create_coord(row: int, column: int, content: object) -> Coordinate:
    '''Create coordinate tuple for given row and column with specified color.'''
    return Coordinate(row, column, content)


def create_row(
        row: int,
        to_col: int,
        from_col: int = 0,
        content: object = {},
    ) -> list[Coordinate]:
    return [create_coord(row, c, content) for c in range(from_col, to_col + 1)]


def create_column(
        column: int,
        to_row: int,
        from_row: int = 0,
        content: object = {},
    ) -> list[Coordinate]:
    return [create_coord(r, column, content) for r in range(from_row, to_row + 1)]


def create_full_rows(
        rows: list[int],
        columns: int,
        content: object = {},
    ) -> list[Coordinate]:
    aux = []
    for row in rows:
        aux.extend(create_row(row, columns - 1, 0, content))
    return aux