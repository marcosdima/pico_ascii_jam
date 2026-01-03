from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from ...entities.entity import Entity


class Parasite:
    __count = 0


    def __init__(self):
        self.id = Parasite.__count
        Parasite.__count += 1
        self.target: 'Entity' = None


    ''' Base class for all parasites. '''
    def set_target(self, target: 'Entity'):
        self.target = target


    ''' Override methods. '''
    def on_update(self, delta_time: float):
        ''' Parasite update called every frame. '''
        print('Parasite on_update called. Consider overriding it.')


    def on_draw(self):
        print('Parasite on_draw called. Consider overriding it.')


    