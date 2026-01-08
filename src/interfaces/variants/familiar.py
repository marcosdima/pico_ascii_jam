from ..base import Base


class Familiar(Base):
    ''' Familiar interface. '''
    def __init__(self):
        self.__parent = None
        self.__children: list['Familiar'] = []
        super().__init__()
        self.update.add_callback(self.__update_children)
        self.draw.add_callback(self.__draw_children)
        self.handle_event.add_callback(self.__handle_event)

    
    def __update_children(self, delta_time):
        ''' Update all children. '''
        for child in self.__children:
            child.update(delta_time)

    
    def __draw_children(self, surface):
        ''' Draw all children. '''
        for child in self.__children:
            child.draw(surface)

        
    def __handle_event(self, event):
        ''' Handle event for all children. '''
        for child in self.__children:
            child.handle_event(event)


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
    

    def has_children(self) -> bool:
        ''' Check if familiar has children. '''
        return len(self.__children) > 0
    

    ''' Transform overrides. '''
    def get_position(self):
        # Get transform position.
        transform_position = super().get_position()

        # If has parent, add parent's position.
        if self.has_parent():
            parent_size = self.__parent.get_position()
            return parent_size + transform_position
        
        return transform_position
        