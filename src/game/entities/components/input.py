import pygame


from .__base import Base
from ....types import Key, MouseButton
from ....utils import Event


## TODO: Focus implementation.


class Input(Base):
    ''' Input interface class. '''
    def __init__(self):
        super().__init__()

        # State.
        self.modifications: dict[Key, Key] = {}
        self.pressed_keys: set[Key] = set()
        
        # Flags.
        self.__mouse_on = False

        # Callbacks.
        self.press_key = Event[Key, None]()
        self.mouse_exit = Event[None]()
        self.mouse_on = Event[None]()
        self.release_key = Event[Key, None]()
        self.press_mouse_button = Event[MouseButton, None]()
        self.release_mouse_button = Event[MouseButton, None]()

        # Set some default callbacks.
        self.press_key.add_callback(lambda key: self.pressed_keys.add(key))
        self.release_key.add_callback(lambda key: self.pressed_keys.discard(key))

        # Set mouse check callbacks.
        self.mouse_on.set_check(lambda: not self.__mouse_on)
        self.mouse_exit.set_check(lambda: self.__mouse_on)
        self.press_mouse_button.set_check(lambda: self.__mouse_on)
        self.release_mouse_button.set_check(lambda: self.__mouse_on)

        # Set event handler.
        self.handle_event.add_callback(self.__handle__event)


    def __handle_key_event(self, event: pygame.event.Event):
        # If key pressed...
        if event.type == pygame.KEYDOWN:
            # Get key.
            key = Key.from_pygame_key(event.key)

            # If key not already pressed...
            if key not in self.pressed_keys:
                self.press_key(key)

        # Else, If key released...
        elif event.type == pygame.KEYUP:
            # Release key.
            self.release_key(Key.from_pygame_key(event.key))


    def __handle_mouse_event(self, event: pygame.event.Event):
        # If mouse button pressed...
        if event.type == pygame.MOUSEBUTTONDOWN:
            button = MouseButton.from_pygame_button(event.button)
            self.press_mouse_button(button)

        # Else, If mouse button released...
        elif event.type == pygame.MOUSEBUTTONUP:
            button = MouseButton.from_pygame_button(event.button)
            self.release_mouse_button(button)

        # Else, If mouse moved...
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            owner_rect = self.get_rect()
            if owner_rect.contains(pygame.Rect(mouse_pos, (1, 1))):
                self.mouse_on()
                self.__mouse_on = True
            elif self.__mouse_on:
                self.mouse_exit()
                self.__mouse_on = False


    def __handle__event(self, event: pygame.event.Event):
        self.__handle_key_event(event)
        self.__handle_mouse_event(event)
