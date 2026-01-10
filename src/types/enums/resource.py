from .__enum import CustomEnum
from ..common.color import Color

class Resource(CustomEnum):
    ROCK = 0
    IRON = 1
    GOLD = 2


    def get_color(self) -> Color:
        '''Get the RGB color associated with the resource.'''
        if self == Resource.ROCK:
            return Color.GRAY
        elif self == Resource.IRON:
            return Color(230, 230, 230).brighter()  # Light gray.
        elif self == Resource.GOLD:
            return Color(255, 215, 0)    # Gold.
        else:
            return Color.WHITE


    @staticmethod
    def from_string(resource_str: str) -> 'Resource':
        '''Convert string to Resource enum.'''
        resource_str = resource_str.lower()
        if resource_str == 'rock':
            return Resource.ROCK
        elif resource_str == 'iron':
            return Resource.IRON
        elif resource_str == 'gold':
            return Resource.GOLD
        else:
            raise ValueError(f'Unknown resource type: {resource_str}')
        

    def __str__(self):
        return self.name.lower()
    