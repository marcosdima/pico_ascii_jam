from .__interface import Interface, abstractmethod
from ..types import Color

class Visible(Interface):
    ''' Visible interface. '''
    def show(self) -> None:
        ''' Set the object as visible. '''
        self.__visible = True


    def hide(self) -> None:
        ''' Set the object as not visible. '''
        self.__visible = False
    

    def is_visible(self) -> bool:
        ''' Check if the object is visible. '''
        return self.__visible


    ''' Interface overrides. '''
    def set_properties(self):
        self.__visible = True
        super().set_properties()
        

    
