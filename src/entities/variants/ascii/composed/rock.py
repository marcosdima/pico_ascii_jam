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
        self.transform_changed.add_callback(self.__on_transform_changed)


    def __on_transform_changed(self, prev, new):
        self.rock.set_transform(size=new.size.to_tuple())


    ''' Composed overrides. '''
    def get_initial_asciis(self) -> list[Ascii]:
        self.rock = Uni30ED()
        return [self.rock]