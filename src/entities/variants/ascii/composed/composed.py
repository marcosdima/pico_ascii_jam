from ..ascii import Ascii, Entity, abstractmethod
from .....types import Color

class Composed(Entity):
    ''' Composed entity class. '''


    def __set_asciis(self):
        ''' Private method to set the Ascii components. '''
        self.asciis = self.get_asciis()


    ''' Abstract methods. '''
    @abstractmethod
    def get_asciis(self) -> list[Ascii]:
        ''' Get the Ascii components that make up this composed entity. '''
        return []


    ''' Entity overrides. '''
    def set_color(self, color: Color):
        super().set_color(color)
        for ascii_entity in self.asciis:
            ascii_entity.set_color(color=self.color)


    ''' Lifecycle methods. '''
    def set_properties(self):
        self.asciis: list[Ascii] = []
        super().set_properties()

        
    def setup(self):
        super().setup()
        self.__set_asciis()
        # Setup each Ascii component.
        for ascii_entity in self.asciis:
            self.modules.family.add_child(ascii_entity.modules.family)