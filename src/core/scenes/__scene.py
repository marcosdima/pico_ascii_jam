from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


from ...entities import Entity
from ..interfaces import Followable


if TYPE_CHECKING:
    from src.game import Game
    

class Scene( ABC):
    '''Base class for all game scenes.'''
    def __init__(self, game: 'Game'):
        self.game = game
        self.entities = self.load_resources()


    def on_update(self, delta_time: float):
        '''Update the scene and its entities.'''
        for entity in self.entities:
            entity.update(delta_time)
            if isinstance(entity, Followable):
                for follower in entity.followers:
                    follower.update(delta_time)
            

    def on_draw(self):
        '''Draw the scene and its entities.'''
        for entity in self.entities:
            entity.draw()
            if isinstance(entity, Followable):
                for follower in entity.followers:
                    follower.draw()


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
    def load_resources(self) -> list[Entity]:
        '''Load necessary resources for the scene.'''
        return []
