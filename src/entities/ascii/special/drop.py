from ..ascii import Ascii
from ....types import Resource, Color
from ....core.interfaces import Collider
from ....types import ColliderGroup


class Drop(Ascii, Collider):
    ''' An ASCII entity that represents a drop character. '''
    def get_default_resource(self) -> Resource:
        ''' Get the resource type of the drop. '''
        return Resource.ROCK
    

    def set_resource(self, resource: Resource):
        ''' Set the resource type of the drop. '''
        self.resource = resource
        self.set_unicode(self.__get_resource_unicode())
        return self
    

    def __get_resource_unicode(self) -> dict[Resource, int]:
        return {
            Resource.ROCK: 0x25CF,   # Unicode character '●'
            Resource.GOLD: 0x25CF,   # Unicode character '●'
            Resource.IRON: 0x25CF,   # Unicode character '●'
        }[self.resource]
    

    ''' Entity life cycle overrides. '''
    def setup(self):
        super().setup()
        self.resource = self.get_default_resource()
        self.set_unicode(self.__get_resource_unicode())
        self.set_transform(scale=(6, 6))


    ''' Entity Overrides. '''
    def get_default_color(self):
        return Color.CYAN
    
    
    def get_default_parasites(self):
        return super().get_default_parasites() + [self.collision]
    

    ''' Collider interface implementation. '''
    def on_collision(self, other_collider: 'Collider'):
        if other_collider.is_player_collider():
            pass#print(f'Recolected {self.resource} from {other_collider.collision_group}')


    ''' Collider interface overrides. '''
    def get_default_collider_group(self) -> 'ColliderGroup':
        return ColliderGroup.ITEM
