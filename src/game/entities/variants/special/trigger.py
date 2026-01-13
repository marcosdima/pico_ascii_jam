import pymunk
from typing import TypeAlias


from ...entity import Entity
from .....types import Size, ColliderGroup
from .....utils import CollisionHandler, Event



TriggerCallback: TypeAlias = Event[pymunk.Arbiter, pymunk.Space, object]


class Trigger(Entity):
    """Base class for trigger entities."""
    def __init__(
        self,
        size: Size,
        lifetime: int = 2 # Seconds.
    ):
        super().__init__()

        # Initialize trigger.
        self.set_size(size)
        self.space_change.add_callback(self.__on_space_set)
        self.__collider_type = ColliderGroup.AREA
        self.set_collision_type(self.__collider_type)

        # Callbacks. These receive (arbiter, space, data).
        self.on_player_enter: callable = lambda arbiter, space, data: True
        self.on_player_exit: callable = lambda arbiter, space, data: None

        self.on_resource_enter: callable = lambda arbiter, space, data: True
        self.on_resource_exit: callable = lambda arbiter, space, data: None
        self.modules.set_debug()
        self.modules.events.assign_time_event(
            name='lifetime',
            event=lambda: self.free(),
            interval=lifetime,
        )

    
    def __on_space_set(self, _):
        '''' Called when the space is set. '''
        # Handle player collisions.
        handler = (
            CollisionHandler(self.__collider_type, ColliderGroup.PLAYER)
                .set_begin(self.__on_player_enter)
                .set_separate(self.__on_player_exit)
        )
        self.set_new_handler(handler)

        # Handle resource collisions.
        resource_handler = (
            CollisionHandler(self.__collider_type, ColliderGroup.RESOURCE)
                .set_begin(self.__on_resource_enter)
                .set_separate(self.__on_resource_exit)
        )
        self.set_new_handler(resource_handler)


    def __on_resource_enter(self, arbiter, space, data):
        """Called when a resource enters the trigger."""
        self.on_resource_enter(arbiter, space, data)
        return True
    

    def __on_resource_exit(self, arbiter, space, data):
        """Called when a resource exits the trigger."""
        self.on_resource_exit(arbiter, space, data)

    
    def __on_player_enter(self, arbiter, space, data):
        """Called when a player enters the trigger."""
        self.on_player_enter(arbiter, space, data)
        return True

    
    def __on_player_exit(self, arbiter, space, data):
        """Called when a player exits the trigger."""
        self.on_player_exit(arbiter, space, data)


    def set_entity_shape(self, entity: Entity) -> None:
        '''Set the trigger's shape to match the entity's shape.'''
        for shape in self.body.shapes:
            shape.entity = entity