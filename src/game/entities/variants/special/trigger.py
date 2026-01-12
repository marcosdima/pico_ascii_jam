import pymunk


from ...entity import Entity
from .....types import Size, ColliderGroup
from .....utils import CollisionHandler, Event


class Trigger(Entity):
    """Base class for trigger entities."""
    def __init__(self, size: Size):
        super().__init__()

        # Initialize trigger.
        self.set_size(size)
        self.modules.set_debug()
        self.space_change.add_callback(self.__on_space_set)

        # Callbacks. These receive (arbiter, space, data).
        self.on_player_enter = Event[[pymunk.Arbiter, pymunk.Space, object]]()
        self.on_player_exit = Event[[pymunk.Arbiter, pymunk.Space, object]]()

    
    def __on_space_set(self, _):
        '''' Called when the space is set. '''
        self.set_collision_type(ColliderGroup.AREA)
        self.create_own_shape()

        # Handle player collisions.
        handler = (
            CollisionHandler(ColliderGroup.AREA, ColliderGroup.PLAYER)
                .set_begin(self.__on_player_enter)
                .set_separate(self.__on_player_exit)
        )
    
        self.set_new_handler(handler)

    
    def __on_player_enter(self, arbiter, space, data):
        """Called when a player enters the trigger."""
        self.on_player_enter(arbiter, space, data)
        return True

    
    def __on_player_exit(self, arbiter, space, data):
        """Called when a player exits the trigger."""
        self.on_player_exit(arbiter, space, data)