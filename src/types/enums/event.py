from .__enum import CustomEnum


class Event(CustomEnum):
    ''' Event enum. '''

    DRAW = 0
    UPDATE = 1
    TRANSFORM_CHANGED = 2