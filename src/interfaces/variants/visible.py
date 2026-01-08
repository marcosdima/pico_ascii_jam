from ..base import Base


class Visible(Base):
    ''' Visible interface. '''
    def __init__(self):
        super().__init__()
        self.__draw = True
        self.draw.set_check(self.is_visible)


    def show(self) -> None:
        ''' Set the object as visible. '''
        self.__draw = True


    def hide(self) -> None:
        ''' Set the object as not visible. '''
        self.__draw = False
    

    def is_visible(self) -> bool:
        ''' Check if the object is visible. '''
        return self.__draw
