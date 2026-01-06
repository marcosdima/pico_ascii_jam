import pygame


from ..module import Module, Transform


class Debug(Module):
    ''' Debug module class. '''


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        super().setup()
        self.update_delay = 10.0 # Seconds.
        self.timeout = 0.0


    def __debug(self, print_message: str):
        print(print_message)
        print('-----------------------------------')


    ''' Module lifecycle methods. '''
    def on_owner_update(self, delta_time: float):
        ''' Called when the owner entity is updated. '''
        super().on_owner_update(delta_time)
        if self.timeout < 0.0:
            self.timeout = self.update_delay
            self.__debug(f'Updating entity id={self.owner.id}')
        else:
            self.timeout -= delta_time
            

    def on_owner_draw(self):
        ''' Called when the owner entity is drawn. '''
        if self.timeout == self.update_delay:
            self.__debug(f'Drawing entity id={self.owner.id} rect: {self.owner.transform.get_rect()}')

        # Draw entity bounding box.
        pygame.draw.rect(
            self.owner.surface,
            self.owner.color.to_pygame_color(),
            self.owner.transform.get_rect(),
            1
        )


    def on_owner_transform_changed(self, prev: Transform, new: Transform):
        ''' Called when the owner entity transform is changed. '''
        self.__debug(f'Entity id={self.owner.id} transform changed from {prev} to {new}')
