from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


from ..entity import Entity


if TYPE_CHECKING:
    from src.game import Game
    

class Scene(Entity, ABC):
    '''Base class for all game scenes.'''
    def __init__(self, game: 'Game'):
        super().__init__(surface=game.screen)
        self.game = game
        self.load_resources()


    ''' Abstract methods. '''
    @abstractmethod
    def handle_event(self, event):
        '''Handle input events.'''
        pass


    @abstractmethod
    def cleanup(self):
        '''Cleanup resources when the scene is destroyed.'''
        pass


    @abstractmethod
    def load_resources(self):
        '''Load necessary resources for the scene.'''
        pass
