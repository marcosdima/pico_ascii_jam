from typing import TYPE_CHECKING
import pymunk, random

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

    def create_damage_trigger(
        self,
        size: tuple,
        offset: tuple = (0, 0),
        damage: float = 10.0,
        lifetime: float = 0.2,
        knockback: float = 350.0,
    ) -> 'Trigger':
        '''Create a damage trigger centered at offset.'''
        from ....entities import Trigger
        trigger = Trigger(size=Size(*size), lifetime=lifetime)
        self.__instantiate(trigger, offset)
        trigger.create_own_shape()

        audio = AudioManager.get_instance()

        def on_player(player):
            # Compute knockback away from owner (source of damage)
            src = pymunk.Vec2d(self.owner.body.position.x, self.owner.body.position.y)
            dst = pymunk.Vec2d(player.body.position.x, player.body.position.y)
            dir_vec = dst - src
            if dir_vec.length > 0:
                kb = dir_vec.normalized() * knockback
                player.body.velocity = kb
            # Apply damage
            if hasattr(player, 'damage'):
                player.damage(damage)
            # Sound
            audio.play_hit_rock()
            return True

        trigger.on_player_enter = on_player
        return trigger
    

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
        player.resources.recolect(of, random.randint(1, 3))
        drop.free()
        drop.ascii.free()
        

    