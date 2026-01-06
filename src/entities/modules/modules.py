from .module import Module
from .variants.family import Family
from .variants.debug import Debug
from .variants.movement import Movement
from .variants.wasd import WASD


class Modules(Module):
    ''' Modules container class. '''
    def set_wasd(self, speed: float = 200.0):
        ''' Set WASD module with given speed. '''
        self.wasd = WASD(self.owner)
        self.wasd.speed = speed


    ''' Module abstract methods. '''
    def setup(self):
        # Set basic modules.
        self.family = Family(self.owner)
        self.debug = Debug(self.owner)
        self.movement = Movement(self.owner)
        