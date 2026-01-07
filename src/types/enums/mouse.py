import pygame


from .__enum import CustomEnum


class MouseButton(CustomEnum):
    ''' Mouse button enum. '''
    LEFT = pygame.BUTTON_LEFT
    MIDDLE = pygame.BUTTON_MIDDLE
    RIGHT = pygame.BUTTON_RIGHT
    ROLL_UP = pygame.BUTTON_WHEELUP
    ROLL_DOWN = pygame.BUTTON_WHEELDOWN

    @classmethod
    def from_pygame_button(cls, button: int) -> 'MouseButton':
        ''' Convert a pygame mouse button integer to a MouseButton enum. '''
        for mb in cls:
            if mb.value == button:
                return mb
        raise ValueError(f'Unknown pygame mouse button: {button}')