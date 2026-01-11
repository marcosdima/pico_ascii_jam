from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
import pygame


from .....types import Size


if TYPE_CHECKING:
    from ...entity import Entity


class Module(ABC):
    ''' Module base class. '''
    def __init__(self, owner: 'Entity'):
        self.owner: 'Entity' = owner

        self.owner.draw.add_callback(self._on_owner_draw)
        self.owner.update.add_callback(self._on_owner_update)
        self.owner.size_change.add_callback(self._on_owner_size_changed)
        self.owner.handle_event.add_callback(self._on_owner_event)

        self.setup()


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        pass


    ''' Module lifecycle methods. '''
    def _on_owner_update(self, delta_time: float):
        ''' Called when the owner entity is updated. '''
        pass


    def _on_owner_draw(self):
        ''' Called when the owner entity is drawn. '''
        pass


    def _on_owner_size_changed(self, prev: Size, new: Size):
        ''' Called when the owner entity size is changed. '''
        pass


    def _on_owner_event(self, event: pygame.event.Event):
        ''' Called when the owner entity receives an event. '''
        pass
