import pymunk


from .__base import Base


class Familiar(Base):
    ''' Familiar interface. '''
    def __init__(self):
        self.__parent = None
        self.__children: list['Familiar'] = []
        self.__joints: dict[int, pymunk.PinJoint] = []

        super().__init__()

        self.update.add_callback(self.__update_children)
        self.draw.add_callback(self.__draw_children)
        self.handle_event.add_callback(self.__handle_event)


    ''' Children management. '''    
    def __update_children(self, delta_time):
        ''' Update all children. '''
        for child in self.__children:
            child.call_update(delta_time)

    
    def __draw_children(self):
        ''' Draw all children. '''
        for child in self.__children:
            child.call_draw(self.base_surface)

        
    def __handle_event(self, event):
        ''' Handle event for all children. '''
        for child in self.__children:
            child.handle_event(event)


    def add_child(self, child: 'Familiar'):
        ''' Add a child .'''
        # Set child parent and save reference.
        child.set_parent(self)
        self.__children.append(child)

        # Create a joint between parent and child.
        joint = pymunk.PinJoint(child.body, self.body)
        self.__joints[child.id] = joint
        self.space.add(joint)


    def remove_child(self, child: 'Familiar'):
        ''' Remove a child. '''
        if child in self.__children:
            joint = self.__joints.pop(child.id)
            self.space.remove(joint)
            self.__children.remove(child)
            child.set_parent(None)

    
    def set_parent(self, parent: 'Familiar'):
        ''' Set familiar parent. '''
        self.__parent = parent
        self.space = parent.space if parent else None


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
    

    