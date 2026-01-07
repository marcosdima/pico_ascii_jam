import pygame


from .__enum import CustomEnum


class Key(CustomEnum):
    ''' Enum class for keyboard keys. '''
    # A-Z keys.
    A = pygame.K_a
    B = pygame.K_b
    C = pygame.K_c
    D = pygame.K_d
    E = pygame.K_e
    F = pygame.K_f
    G = pygame.K_g
    H = pygame.K_h
    I = pygame.K_i
    J = pygame.K_j
    K = pygame.K_k
    L = pygame.K_l
    M = pygame.K_m
    N = pygame.K_n
    O = pygame.K_o
    P = pygame.K_p
    Q = pygame.K_q
    R = pygame.K_r
    S = pygame.K_s
    T = pygame.K_t
    U = pygame.K_u
    V = pygame.K_v
    W = pygame.K_w
    X = pygame.K_x
    Y = pygame.K_y
    Z = pygame.K_z

    # Number keys.
    ZERO = pygame.K_0
    ONE = pygame.K_1
    TWO = pygame.K_2
    THREE = pygame.K_3
    FOUR = pygame.K_4
    FIVE = pygame.K_5
    SIX = pygame.K_6
    SEVEN = pygame.K_7
    EIGHT = pygame.K_8
    NINE = pygame.K_9

    # Arrow keys.
    LEFT = pygame.K_LEFT
    RIGHT = pygame.K_RIGHT
    UP = pygame.K_UP
    DOWN = pygame.K_DOWN

    # Modifier keys.
    SHIFT = pygame.K_LSHIFT
    CTRL = pygame.K_LCTRL
    ALT = pygame.K_LALT

    # Space and Enter.
    SPACE = pygame.K_SPACE
    ENTER = pygame.K_RETURN


    @classmethod
    def from_pygame_key(cls, pygame_key: int) -> 'Key':
        '''Map a raw pygame key code to the Key enum. Raises ValueError if unmapped.'''
        for key in cls:
            if key.value == pygame_key:
                return key
        raise ValueError(f'Unmapped pygame key code: {pygame_key}')
