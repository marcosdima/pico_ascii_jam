from .__enum import CustomEnum


class ColliderGroup(CustomEnum):
    ''' Enumeration for collider groups. '''
    DEFAULT = 0
    PLAYER = 1
    ENEMY = 2
    ITEM = 3
    ENVIRONMENT = 4