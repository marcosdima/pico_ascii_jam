from typing import TYPE_CHECKING


from .__module import Module
from .....types import Resource, Size, ColliderGroup
from .....utils import AudioManager


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
        self.__parasite(entity=entity)
        return entity


    def create_trigger(
        self,
        size: tuple,
        offset: tuple = (0, 0),
    ) -> 'Trigger':
        '''Create a Trigger entity.'''
        from ....entities import Trigger
        trigger = Trigger(size)
        self.__instantiate(trigger, offset)
        trigger.create_own_shape()
        return trigger
    

    def create_drop(
        self,
        of: Resource,
        offset: tuple = (0, 0),
        timeout: int = 2,
    ) -> 'Trigger':
        '''Create a Drop entity.'''
        from ....entities import CF, Trigger
        drop = Trigger(size=Size(50, 50), lifetime=timeout, collider_type=ColliderGroup.ITEM)
        self.__instantiate(drop, offset)
        drop.create_own_shape()
        
        # Set ASCII representation based on resource.
        ascii_entity = CF(5)
        ascii_entity.set_color(of.get_color()) 
        self.__instantiate(ascii_entity, offset)

        # Set drop with global reference.
        drop.on_player_enter = lambda p, d=drop, o=of: self.__recolect_drop(p, d, o)
        drop.ascii = ascii_entity
        self.__parasite( entity=drop)

        return drop
    

    def __parasite(self, entity: 'Entity', host: 'Entity' = None):
        '''Parasite an entity to the owner.'''
        from ....entities import GLOBAL
        owner = GLOBAL if host is None else host
        entity.set_space(owner.space)
        owner.space_change.add_callback(lambda s: entity.set_space(s))
        owner.update.add_callback(entity.update)
        owner.handle_event.add_callback(entity.handle_event)
        owner.draw.add_callback(lambda: entity.call_draw(owner.base_surface))


    def __recolect_drop(self, player, drop: 'Trigger', of: Resource):
        # Play hit sound
        audio = AudioManager.get_instance()
        audio.play_pickup()
        player.resources.recolect(of, 1)
        drop.free()
        drop.ascii.free()
        

    