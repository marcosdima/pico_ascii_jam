from .rock import Rock
from .....types import Resource, Color


class Gold(Rock):
    ''' An ASCII entity that represents a gold rock character. '''
    def get_resource(self) -> Resource:
        ''' Get the resource type of the gold rock. '''
        return Resource.GOLD
    

    ''' Entity Overrides. '''
    def get_default_color(self):
        return Color.YELLOW