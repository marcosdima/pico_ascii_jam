from ..ascii import Ascii, Entity, abstractmethod
from .....types import Color

class Composed(Entity):
    ''' Composed entity class. '''
    def __init__(self):
        super().__init__()

        # Initialize Ascii components.
        self.__asciis: list[Ascii] = self.get_initial_asciis()
        
        # Add Ascii components as children.
        for ascii in self.__asciis:
            self.add_child(ascii)


    def get_asciis(self) -> list[Ascii]:
        ''' Access to Ascii components. '''
        return self.__asciis
    

    ''' Entity overrides. '''
    def get_size(self):
        if not self.__asciis:
            return super().get_size()
        
        aux = self.get_asciis()[0].get_size()
        for ascii in self.get_asciis()[1:]:
            aux += ascii.get_size()
            
        return aux


    ''' Abstract methods. '''
    @abstractmethod
    def get_initial_asciis(self) -> list[Ascii]:
        ''' Get the Ascii components that make up this composed entity. '''
        return []


        
    