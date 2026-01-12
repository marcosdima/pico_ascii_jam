import pygame
from typing import Literal

from .__module import Module
from .....types import Color


class Debug(Module):
    ''' Debug module class with filtered logging capabilities. '''
    def __debug(self, message: str, category: str):
        ''' Centralized debug message handling. '''
        if category not in self.enabled:
            return
        
        print(f'[{category.upper()}] Entity id={self.owner.id}: {message}')


    def setup(self):
        # Debug configuration.
        self.update_delay = 5.0  # Seconds between update logs.
        self.timeout = 0.0
        
        # Enabled  debug categories.
        self.enabled: set[
            Literal[
                'update',
                'draw',
                'size',
                'events',
                'keyboard',
                'mouse',
                'bounding_box',
                'color',
                'collisions',
            ]
        ] = set(
            (
                # 'update',          # Periodic update logs
                # 'draw',           # Drawing logs
                'size',            # size change logs
                # 'events',          # Pygame events logs
                # 'keyboard',        # Keyboard input logs
                # 'mouse',           # Mouse input logs
                'bounding_box',    # Draw bounding box
                'color',
                'collisions',
            )
        )

        # Connect draw callback
        self.owner.draw.add_callback(self._on_owner_draw)

    
    def _on_owner_draw(self):
        '''Draw debug visualization for collision shapes.'''
        if 'bounding_box' not in self.enabled:
            return
        
        for shape in self.owner.body.shapes:
            bb = shape.bb
            # Calculate bounding box dimensions and center
            width = bb.right - bb.left
            height = bb.top - bb.bottom
            center_x = (bb.left + bb.right) / 2
            center_y = (bb.bottom + bb.top) / 2
            
            # Draw outline rectangle
            surface = pygame.Surface((width, height), pygame.SRCALPHA)
            pygame.draw.rect(surface, Color.RED.to_pygame_color(), surface.get_rect(), 2)
            
            rect = surface.get_rect(center=(center_x, center_y))
            self.owner.base_surface.blit(surface, rect)