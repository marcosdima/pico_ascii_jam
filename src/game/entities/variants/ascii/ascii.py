from abc import ABC, abstractmethod


from ...entity import Entity
from .....types import Pixel, Color


class Ascii(Entity, ABC):
    """Base class for ASCII-based entities."""
    def __init__(self):
        super().__init__()

        # Set grid layout based on ASCII tiles.
        tiles = self.get_tiles()
        grid_dims = self._compute_grid_dimensions(tiles)
        self.modules.set_layout('grid', grid_dims)
        
        # Set grid layout based on ASCII tiles and populate tile entities.
        self._tile_entities: dict[tuple[int, int], Entity] = {}
        layout = self.modules.layout
        
        for pixel in tiles:
            tile_entity = Entity()
            tile_entity.set_color(pixel.color)
            tile_entity.modules.set_background()

            pixel_pos, _ = pixel.to_tuple()
            layout.add_component(tile_entity, {'coords': pixel_pos})
            self._tile_entities[pixel_pos] = tile_entity

        self.on_set_color.add_callback(self._on_color_changed)
        

    def _on_color_changed(self, new_color: Color):
        """Update tile colors when the ASCII entity color changes."""
        tiles = self.get_tiles()
        for pixel in tiles:
            pixel_pos, pixel_color = pixel.to_tuple()
            if pixel_pos in self._tile_entities:
                self._tile_entities[pixel_pos].set_color(pixel_color or new_color)
            

    def _set_pixel(self, column: int, row: int, color: Color = None) -> Pixel:
        """Get pixel instace."""
        return Pixel(column, row, color or self.color)


    def _compute_grid_dimensions(self, tiles: list[Pixel]) -> dict:
        """Calculate grid dimensions from a list of tiles."""
        if not tiles:
            return {'rows': 0, 'columns': 0}
        
        max_x = max(pixel.x for pixel in tiles)
        max_y = max(pixel.y for pixel in tiles)
        
        return {
            'rows': max_y + 1,
            'columns': max_x + 1,
        }
        
    
    def set_space(self, space):
        """Propagate space assignment to tile entities."""
        super().set_space(space)
        for tile in self._tile_entities.values():
            tile.set_space(space)

        
    @abstractmethod
    def get_ascii_unicode(self) -> int:
        """Return the Unicode character representing the ASCII entity."""
        pass


    @abstractmethod
    def get_tiles(self) -> list[Pixel]:
        """Return a matrix of pixels representing the ASCII entity tiles."""
        pass





