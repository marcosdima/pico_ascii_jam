from .rock import Rock
from .....types import Resource


class Iron(Rock):
    ''' An ASCII entity that represents an iron rock character. '''
    def get_resource(self) -> Resource:
        ''' Get the resource type of the iron rock. '''
        return Resource.IRON
    

    