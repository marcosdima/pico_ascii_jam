from ..parasites import Collision
from ...types import ColliderGroup


class Collider:
    ''' Interface for collidable entities. '''
    def __init__(self):
        super().__init__()
        self.collision = Collision(
            on_collision_callback=self.on_collision,
            on_end_collision_callback=self.on_end_collision,
            on_keep_collision_callback=self.on_keep_collision
        )
        self.collision_group = self.get_default_collider_group()


    def get_default_collider_group(self) -> ColliderGroup:
        ''' Get the default collider group for the entity. '''
        return ColliderGroup.DEFAULT


    def on_collision(self, other_collider: 'Collider'):
        ''' Called when a collision with another entity occurs. '''
        pass


    def on_end_collision(self, other_collider: 'Collider'):
        ''' Called when a collision with another entity ends. '''
        pass


    def on_keep_collision(self, other_collider: 'Collider'):
        ''' Called while a collision with another entity is ongoing. '''
        pass


    def is_player_collider(self) -> bool:
        ''' Check if the collider belongs to a player entity. '''
        return self.collision_group == ColliderGroup.PLAYER
    