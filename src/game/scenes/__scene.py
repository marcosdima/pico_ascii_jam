from typing import TYPE_CHECKING


from ..entities import Entity


if TYPE_CHECKING:
    from game import Game
    

by_z_index = lambda e: e.z_index


class Scene:
    '''Base class for all game scenes.'''
    def __init__(self, game: 'Game' = None):
        super().__init__()
        self.game: 'Game' = game
        self.__entities: list[Entity] = []
        self.setup()

    
    def setup(self):
        '''Setup the scene. Override in subclasses.'''
        pass


    def add_entity(self, entity: Entity) -> None:
        '''Add an entity to the scene.'''
        entity.set_space(self.game.space)
        self.__entities.append(entity)
        self.__entities.sort(key=by_z_index)

    
    def remove_entity(self, entity: Entity) -> None:
        '''Remove an entity from the scene.'''
        self.__entities.remove(entity)
        entity.space = None


    def draw(self, surface) -> None:
        '''Draw the scene.'''
        for entity in self.__entities:
            entity.call_draw(surface)


    def update(self, delta_time: float) -> None:
        '''Update the scene.'''
        for entity in self.__entities:
            entity.call_update(delta_time)
