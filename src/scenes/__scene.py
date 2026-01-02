from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.game import Game


class Scene(ABC):
    '''Base class for all game scenes.'''
    def __init__(self, game: 'Game'):
        self.game = game


    ''' Abstract methods. '''
    @abstractmethod
    def handle_event(self, event):
        '''Handle input events.'''
        pass


    @abstractmethod
    def update(self, dt):
        '''Update scene logic.'''
        pass


    @abstractmethod
    def draw(self, screen):
        '''Render the scene to the screen.'''
        pass
