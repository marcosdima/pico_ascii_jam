from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
import pygame


from ...types import Event, Transform


if TYPE_CHECKING:
    from ..entity import Entity


class Module(ABC):
    ''' Module base class. '''
    def __init__(self, owner: 'Entity'):
        self.owner: 'Entity' = owner
        self.setup()


    ''' Abstract methods. '''
    @abstractmethod
    def setup(self):
        ''' Setup the module. '''
        self.owner.add_event_callback(Event.DRAW, self.on_owner_draw)
        self.owner.add_event_callback(Event.UPDATE, self.on_owner_update)
        self.owner.add_event_callback(Event.TRANSFORM_CHANGED, self.on_owner_transform_changed)
        self.owner.add_event_callback(Event.PYGAME_EVENT, self.on_owner_event)


    ''' Module lifecycle methods. '''
    def on_owner_update(self, delta_time: float):
        ''' Called when the owner entity is updated. '''
        pass


    def on_owner_draw(self):
        ''' Called when the owner entity is drawn. '''
        pass


    def on_owner_transform_changed(self, prev: Transform, new: Transform):
        ''' Called when the owner entity transform is changed. '''
        pass


    def on_owner_event(self, event: pygame.event.Event):
        ''' Called when the owner entity receives an event. '''
        pass
