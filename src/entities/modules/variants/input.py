import pygame
from typing import Literal


from ..module import Module
from ....types import Key, MouseButton


class Input(Module):
    ''' Input module class. '''
    def __handle_key_event(self, event: pygame.event.Event):
        if event.type == pygame.KEYDOWN:
            key = Key.from_pygame_key(event.key)
            if key not in self.pressed_keys:
                self.press_key(key)
        elif event.type == pygame.KEYUP:
            key = Key.from_pygame_key(event.key)
            self.release_key(key)


    def __handle_mouse_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = MouseButton.from_pygame_button(event.button)
            if self.__mouse_on:
                self.press_mouse_button(button)
        elif event.type == pygame.MOUSEBUTTONUP:
            button = MouseButton.from_pygame_button(event.button)
            self.release_mouse_button(button)
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if self.owner.transform.get_rect().contains(pygame.Rect(mouse_pos, (1, 1))):
                self.mouse_on()
                self.__mouse_on = True
            elif self.__mouse_on:
                self.mouse_exit()
                self.__mouse_on = False


    def press_key(self, key: Key) -> bool:
        self.pressed_keys.add(key)
        for callback in self.pressed_callbacks.get(key.value, []):
            callback()


    def release_key(self, key: Key) -> bool:
        self.pressed_keys.discard(key)
        for callback in self.released_callbacks.get(key.value, []):
            callback()


    def press_mouse_button(self, button: MouseButton) -> bool:
        for callback in self.mouse_pressed_callbacks.get(button.value, []):
            callback()


    def release_mouse_button(self, button: MouseButton) -> bool:
        for callback in self.mouse_released_callbacks.get(button.value, []):
            callback()


    def mouse_on(self) -> bool:
        for callback in self.mouse_on_callbacks:
            callback()


    def mouse_exit(self) -> bool:
        for callback in self.mouse_exit_callbacks:
            callback()


    ''' Add callback methods. '''
    def add_key_callback(
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

    
    def add_mouse_button_callback(
        self,
        to: Literal['pressed', 'released'],
        button: MouseButton,
        callback: callable,
    ):
        ''' Add a callback for a mouse button event. '''
        if to == 'pressed':
            mouse_callbacks = self.mouse_pressed_callbacks
        elif to == 'released':
            mouse_callbacks = self.mouse_released_callbacks
        
        # Check if key already has callbacks.
        if button not in mouse_callbacks:
            mouse_callbacks[button] = []
        
        mouse_callbacks[button].append(callback)


    def add_mouse_callback(
        self,
        to: Literal['on', 'exit'],
        callback: callable,
    ):
        ''' Add a callback for a mouse event. '''
        if to == 'on':
            self.mouse_on_callbacks.append(callback)
        elif to == 'exit':
            self.mouse_exit_callbacks.append(callback)

            
    ''' Abstract methods. '''
    def setup(self):
        super().setup()
        self.modifications: dict[Key, Key] = {}
        self.pressed_keys: set[Key] = set()
        
        # Flags.
        self.__mouse_on = False

        # Callbacks.
        self.pressed_callbacks: dict[Key, list] = {}
        self.released_callbacks: dict[Key, list] = {}
        self.mouse_pressed_callbacks: dict[MouseButton, list] = {}
        self.mouse_released_callbacks: dict[MouseButton, list] = {}
        self.mouse_on_callbacks: list = []
        self.mouse_exit_callbacks: list = []


    ''' Module lifecycle methods. '''
    def on_owner_event(self, event: pygame.event.Event):
        super().on_owner_event(event)
        self.__handle_key_event(event)
        self.__handle_mouse_event(event)
        
        
