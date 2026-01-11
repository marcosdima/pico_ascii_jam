import pymunk

from .__module import Module
from .....utils import CollisionHandler
from .....types import ColliderGroup


class Collision(Module):
    ''' Collision module class. '''
    def setup(self):
        self.handlers: set[CollisionHandler] = set()
        self.collision_type: int = ColliderGroup.DEFAULT.value


    def set_new_handler(self, collision_handler: CollisionHandler):
        ''' Set a new collision handler. '''
        if not collision_handler in self.handlers:
            self.handlers.add(collision_handler)
            self.owner.space.on_collision(*collision_handler.as_params())
    

    def get_handler(
        self,
        a: int | tuple[int | int] = 1,
        b: int = None,
    ) -> set[CollisionHandler]:
        if isinstance(a, tuple):
            a, b = a
        elif not b:
            b = a
        
        for handler in self.handlers:
            if handler.a == a and handler.b == b:
                return handler
        
        print(f'No collision handler found for groups {a} and {b}.')
        return None
    

    def set_collision_type(self, coll_type: int | ColliderGroup):
        ''' Set collision type for owner shapes. '''
        if isinstance(coll_type, ColliderGroup):
            coll_type = coll_type.value
        self.collision_type = coll_type
        for shape in self.owner.body.shapes:
            shape.collision_type = coll_type
    

    def create_own_shape(self):
        owner = self.owner

        shape = pymunk.Poly.create_box(owner.body, owner.size.to_tuple())
        owner.space.add(shape)

        shape.collision_type = self.collision_type
        

    
