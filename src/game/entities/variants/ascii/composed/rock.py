from .composed import Composed
from ..base.uni30ED import Uni30ED
from ..ascii import Ascii
from .....types import Resource

class Rock(Composed):
    ''' Rock entity class. '''
    def __init__(self, resource: Resource):
        super().__init__()
        self.resource = resource
        self.rock.set_color(self.resource.get_color())
        self.on_size_change.add_callback(self.__on_size_change)


    def __on_size_change(self, prev, new):
        self.rock.set_transform(size=new.to_tuple())


    ''' Composed overrides. '''
    def get_initial_asciis(self) -> list[Ascii]:
        self.rock = Uni30ED()
        return [self.rock]