import pygame


from ..module import Module, Transform


class Background(Module):
    ''' Background module class. '''


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        super().setup()
        self.update_delay = 10.0 # Seconds.
        self.timeout = 0.0


    ''' Module lifecycle methods. '''
    def on_owner_draw(self, surface):
        ''' Called when the owner entity is drawn. '''
        if self.timeout == self.update_delay:
            self.__debug(f'Drawing entity id={self.owner.id} rect: {self.owner.transform.get_rect()}')

        # Draw a rectangle.
        pygame.draw.rect(
            surface,
            self.owner.color.to_pygame_color(),
            self.owner.get_rect(),
        )

