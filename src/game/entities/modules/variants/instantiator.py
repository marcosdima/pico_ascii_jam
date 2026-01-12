from .__module import Module
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...entity import Entity
    from ...variants.special.trigger import Trigger


class Instantiator(Module):
    ''' Module that instantiates entities. '''
    def setup(self):
        self.instances: list['Entity'] = []
    
    
    def __instantiate(self, entity: 'Entity', offset: tuple = (0, 0)):
        '''Instantiate an entity.'''
        entity.body.position = offset
        self.instances.append(entity)
        
        # Parasite owner.
        owner = self.owner
        owner.space_change.add_callback(lambda s: entity.set_space(s))
        owner.update.add_callback(entity.update)
        #owner.draw.add_callback(entity.draw)
        owner.handle_event.add_callback(entity.handle_event) 

        return entity

        
    def create_trigger(self, size: tuple, offset: tuple = (0, 0)) -> 'Trigger':
        '''Create a Trigger entity.'''
        from ...variants.special.trigger import Trigger
        trigger = Trigger(size)
        return self.__instantiate(trigger, offset)