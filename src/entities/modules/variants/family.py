from ..module import Module


class Family(Module):
    ''' Family module. '''
    def add_child(self, child: 'Family'):
        ''' Add a child .'''
        child.set_parent(self)
        self.__children.append(child)

    
    def set_parent(self, parent: 'Family'):
        ''' Set familiar parent. '''
        self.__parent = parent


    def get_parent(self):
        ''' Get familiar parent. '''
        return self.__parent.owner
    

    def get_children(self) -> list['Family']:
        ''' Get familiar children. '''
        return self.__children
    

    def has_parent(self) -> bool:
        ''' Check if familiar has a parent. '''
        return self.__parent is not None
    
    
    ''' Interface event methods. '''
    def on_owner_draw(self):
        ''' Interface: Call all draw event callbacks. '''
        super().on_owner_draw()
        for child in self.__children:
            child.owner.on_draw()


    def on_owner_update(self, delta_time: float):
        ''' Interface: Call all update event callbacks. '''
        super().on_owner_update(delta_time)
        for child in self.__children:
            child.owner.on_update(delta_time)
        

    ''' Module abstract methods. '''
    def setup(self):
        super().setup()
        self.__parent: 'Family' = None
        self.__children: list['Family'] = []
            
