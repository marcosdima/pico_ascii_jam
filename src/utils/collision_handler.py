import pymunk
from enum import Enum


from ..types import ColliderGroup


class CollisionHandler:
    ''' Collision handler class. '''
    def __init__(self, a: ColliderGroup, b: ColliderGroup):
        self.a = a
        self.b = b
        self.begin: callable = lambda arbiter, space, data: True
        self.pre_solve: callable = lambda arbiter, space, data: True
        self.post_solve: callable = lambda arbiter, space, data: None
        self.separate: callable = lambda arbiter, space, data: None


    def set_begin(self, func: callable) -> 'CollisionHandler':
        ''' Set the begin collision callback. '''
        self.begin = func
        return self


    def set_pre_solve(self, func: callable) -> 'CollisionHandler':
        ''' Set the pre-solve collision callback. '''
        self.pre_solve = func
        return self


    def set_post_solve(self, func: callable) -> 'CollisionHandler':
        ''' Set the post-solve collision callback. '''
        self.post_solve = func
        return self

    def set_separate(self, func: callable) -> 'CollisionHandler':
        ''' Set the separate collision callback. '''
        self.separate = func
        return self
    

    def as_params(self) -> tuple:
        ''' Return the collision handler as parameters tuple. '''
        return (self.a.value, self.b.value, self.begin, self.pre_solve, self.post_solve, self.separate)
    

    def __eq__(self, value):
        if not isinstance(value, CollisionHandler):
            return False
        return (self.a, self.b) == (value.a, value.b)
    

    def __hash__(self):
        return hash((self.a, self.b))