import pygame
from typing import Literal

from .__module import Module
from .....types import Size


class Debug(Module):
    ''' Debug module class with filtered logging capabilities. '''
    def __debug(self, message: str, category: str):
        ''' Centralized debug message handling. '''
        if category not in self.enabled:
            return
        
        print(f'[{category.upper()}] Entity id={self.owner.id}: {message}')


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        super().setup()

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
                #'update',          # Periodic update logs
                # 'draw',           # Drawing logs
                'size',            # size change logs
                #'events',          # Pygame events logs
                #'keyboard',        # Keyboard input logs
                'mouse',           # Mouse input logs
                'bounding_box',    # Draw bounding box
                'color',
                'collisions',
            )
        )