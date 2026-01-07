import pygame
from typing import Literal

from ..module import Module, Transform


class Debug(Module):
    ''' Debug module class. '''


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        super().setup()

        self.update_delay = 10.0 # Seconds.
        self.timeout = 0.0
        self.print = False # Change to False to disable debug printing.
        self.filters: set[Literal['events', 'keys', 'mouse']] = set() # List of debug filters

        # Input debug.
        self.owner.modules.input.add_mouse_callback(
            to='on',
            callback=(
                lambda:
                    self.__debug(
                        print_message=f'Entity id={self.owner.id} mouse on',
                        force='mouse' not in self.filters
                    )
            )
        )
        self.owner.modules.input.add_mouse_callback(
            to='exit',
            callback=(
                lambda:
                    self.__debug(
                        print_message=f'Entity id={self.owner.id} mouse exit',
                        force='mouse' not in self.filters
                    )
            )
        )
        self.owner.modules.input.add_mouse_button_callback(
            to='pressed',
            button=pygame.BUTTON_LEFT,
            callback=(
                lambda:
                    self.__debug(
                        print_message=f'Entity id={self.owner.id} mouse button LEFT pressed',
                        force='mouse' not in self.filters
                    )
            )
        )
        self.owner.modules.input.add_mouse_button_callback(
            to='released',
            button=pygame.BUTTON_LEFT,
            callback=(
                lambda:
                    self.__debug(
                        print_message=f'Entity id={self.owner.id} mouse button LEFT released',
                        force='mouse' not in self.filters
                    )
            )
        )
        self.owner.modules.input.add_key_callback(
            to='pressed',
            target=pygame.K_SPACE,
            callback=(
                lambda:
                    self.__debug(
                        print_message=f'Entity id={self.owner.id} key SPACE pressed',
                        force='keys' not in self.filters
                    )
            )
        )


    def __debug(self, print_message: str, force: bool = False):
        if not self.print and not force:
            return
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
        super().on_owner_draw()
        if self.timeout == self.update_delay:
            self.__debug(f'Drawing entity id={self.owner.id} rect: {self.owner.transform.get_rect()}')

        # Draw entity bounding box.
        pygame.draw.rect(
            self.owner.surface,
            self.owner.color.to_pygame_color(),
            self.owner.get_rect(),
            1,
        )


    def on_owner_transform_changed(self, prev: Transform, new: Transform):
        ''' Called when the owner entity transform is changed. '''
        super().on_owner_transform_changed(prev, new)
        self.__debug(f'Entity id={self.owner.id} transform changed from {prev} to {new}')


    def on_owner_event(self, event: pygame.event.Event):
        ''' Called when the owner entity receives an event. '''
        super().on_owner_event(event)
        self.__debug(f'Entity id={self.owner.id} received event: {event}')
