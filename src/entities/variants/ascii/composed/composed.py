from ..ascii import Ascii, Entity, abstractmethod
from .....types import Color

class Composed(Entity):
    ''' Composed entity class. '''


    ''' Abstract methods. '''
    @abstractmethod
    def set_asciis(self) -> list[Ascii]:
        ''' Get the Ascii components that make up this composed entity. '''
        return []


    ''' Entity overrides. '''
    def set_color(self, color: Color):
        super().set_color(color)

        if not hasattr(self, 'asciis'):
            return
        
        for ascii_entity in self.asciis:
            ascii_entity.set_color(color=self.color)


    ''' Lifecycle methods. '''
    def set_properties(self):
        super().set_properties()
        self.asciis: list[Ascii] = []

        
    def setup(self):
        super().setup()
        self.asciis = self.set_asciis()

        # Setup each Ascii component.
        for ascii_entity in self.asciis:
            self.modules.family.add_child(ascii_entity.modules.family)