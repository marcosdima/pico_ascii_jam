from abc import ABC, abstractmethod
import pygame


class UI(ABC):
    '''Base class for UI elements.'''
    def __init__(self, surface: pygame.Surface):
        self.base_surface = surface
        self.setup()


    @abstractmethod
    def setup(self):
        '''Setup the UI element.'''
        pass


    @abstractmethod
    def draw(self):
        '''Draw the UI element.'''
        pass


    def update(self, delta_time: float):
        '''Update the UI element. Override if needed.'''
        pass
