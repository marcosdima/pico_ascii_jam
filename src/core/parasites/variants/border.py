import pygame
from ..parasite import Parasite


class Border(Parasite):
    ''' A parasite that draws a border around the target entity. '''
    def on_draw(self):
        target = self.target
        x, y = target.transform.position.to_tuple()
        w, h = target.transform.get_scaled_size().to_tuple()
        color = target.get_color().to_rgb()
        
        # Draw border lines
        pygame.draw.line(target.surface, color, (x, y), (x + w, y))                    # Top
        pygame.draw.line(target.surface, color, (x, y + h), (x + w, y + h))            # Bottom
        pygame.draw.line(target.surface, color, (x, y), (x, y + h))                    # Left
        pygame.draw.line(target.surface, color, (x + w, y), (x + w, y + h))            # Right

    
    def on_update(self, dt):
        pass