from .__base import Base


class Familiar(Base):
    ''' Familiar interface. '''
    def __init__(self):
        self.__parent = None
        self.__children: list['Familiar'] = []

        super().__init__()

        self.update.add_callback(self.__update_children)
        self.draw.add_callback(self.__draw_children)
        self.handle_event.add_callback(self.__handle_event)
        self.transform_changed.add_callback(self.__update_world_transform)


    def __update_world_transform(self, prev, new):
        ''' Update the world transform based on parent transforms. '''
        copy = self.transform.copy()
        if self.has_parent():
            parent_transform = self.__parent.get_world_transform()
            copy.position = self.rotate_point(
                copy.position,
                parent_transform.rotation
            )
            self.world_transform = copy + parent_transform
        else:
            self.world_transform = copy
        

    ''' Children management. '''    
    def __update_children(self, delta_time):
        ''' Update all children. '''
        for child in self.__children:
            child.call_update(delta_time)

    
    def __draw_children(self):
        ''' Draw all children. '''
        for child in self.__children:
            child.__update_world_transform(None, None)
            child.call_draw(self.base_surface)

        
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
    

    