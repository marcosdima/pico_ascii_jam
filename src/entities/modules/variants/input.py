import pygame
from typing import Literal


from ..module import Module
from ....types import Key


class Input(Module):
    ''' Input module class. '''
    def press(self, key: Key) -> bool:
        self.pressed_keys.add(key)
        for callback in self.pressed_callbacks.get(key, []):
            callback()


    def release(self, key: Key) -> bool:
        self.pressed_keys.discard(key)
        for callback in self.released_callbacks.get(key, []):
            callback()


    def add_callback(
        self,
        to: Literal['pressed', 'released'],
        target: Key,
        callback: callable,
    ):
        ''' Add a callback for a key event. '''
        if to == 'pressed':
            key_callbacks = self.pressed_callbacks
        elif to == 'released':
            key_callbacks = self.released_callbacks

        # Check if key already has callbacks.
        if target not in key_callbacks:
            key_callbacks[target] = []
        
        key_callbacks[target].append(callback)
            


    ''' Abstract methods. '''
    def setup(self):
        super().setup()
        self.modifications: dict[Key, Key] = {}
        self.pressed_keys: set[Key] = set()
        self.pressed_callbacks: dict[Key, list] = {}
        self.released_callbacks: dict[Key, list] = {}


    ''' Module lifecycle methods. '''
    def on_owner_event(self, event: pygame.event.Event):
        super().on_owner_event(event)
        if event.type == pygame.KEYDOWN:
            key = Key.from_pygame_key(event.key)
            if key not in self.pressed_keys:
                self.press(key)
        elif event.type == pygame.KEYUP:
            key = Key.from_pygame_key(event.key)
            self.release(key)

