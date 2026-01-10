from ..base import Base
from ...types import Position


class Familiar(Base):
    ''' Familiar interface. '''
    def __init__(self):
        self.__parent = None
        self.__children: list['Familiar'] = []

        super().__init__()
        
        self.update.add_callback(self.__update_children)
        self.draw.add_callback(self.__draw_children)
        self.handle_event.add_callback(self.__handle_event)


    ''' Transform overrides. '''
    def get_global_position(self) -> Position:
        ''' Get the start point of the familiar. '''
        global_pos = super().get_global_position()
        if self.has_parent():
            return self.__parent.get_global_position() + global_pos
        return global_pos
        

    ''' Children management. '''    
    def __update_children(self, delta_time):
        ''' Update all children. '''
        for child in self.__children:
            child.call_update(delta_time)

    
    def __draw_children(self):
        ''' Draw all children. '''
        for child in self.__children:
            child.call_draw(self.surface)

        
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
    

    