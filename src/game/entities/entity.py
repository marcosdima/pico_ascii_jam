from .modules import Modules
from .components import Components


class Entity(Components):
    ''' Entity base class. '''
    def __str__(self):
        return f'<Entity id={self.id}>'


    ''' Python special methods. '''
    def __init__(self):
        super().__init__()
        
        # Initialize components.
        self.modules = Modules(self)


    