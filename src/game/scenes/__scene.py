from abc import ABC, abstractmethod
from typing import TYPE_CHECKING


from ...entities import Entity


if TYPE_CHECKING:
    from game import Game
    

by_z_index = lambda e: e.transform.z_index


class Scene(ABC):
    '''Base class for all game scenes.'''
    def __init__(self):
        super().__init__()
        self.main_entity: Entity = Entity()


    def add_entity(self, entity: Entity) -> None:
        '''Add an entity to the scene.'''
        self.main_entity.add_child(entity)

    
    def remove_entity(self, entity: Entity) -> None:
        '''Remove an entity from the scene.'''
        self.main_entity.remove_child(entity)

    
    def set_game(self, game: 'Game') -> None:
        '''Update the scene and its entities.'''
        game.main_scene = self
        self.game = game