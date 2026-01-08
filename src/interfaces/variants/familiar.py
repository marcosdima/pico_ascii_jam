from ..base import Base


class Familiar(Base):
    ''' Familiar interface. '''
    def __init__(self):
        self.__parent = None
        self.__children: list['Familiar'] = []
        super().__init__()


    def add_child(self, child: 'Familiar'):
        ''' Add a child .'''
        child.set_parent(self)
        self.__children.append(child)


    def remove_child(self, child: 'Familiar'):
        ''' Remove a child. '''
        if child in self.__children:
            self.__children.remove(child)
            child.set_parent(None)

    
    def set_parent(self, parent: 'Familiar'):
        ''' Set familiar parent. '''
        self.__parent = parent


    def get_parent(self):
        ''' Get familiar parent. '''
        return self.__parent
    

    def get_children(self) -> list['Familiar']:
        ''' Get familiar children. '''
        return self.__children
    

    def has_parent(self) -> bool:
        ''' Check if familiar has a parent. '''
        return self.__parent is not None
    

    ''' Overrides. '''
    def set_properties(self):
        self.__parent: 'Familiar' = None
        self.__children: list['Familiar'] = []
        super().set_properties()


    ''' Transform overrides. '''
    def get_position(self):
        # Get transform position.
        transform_position = super().get_position()

        # If has parent, add parent's position.
        if self.has_parent():
            parent_size = self.__parent.get_position()
            return parent_size + transform_position
        
        return transform_position
        