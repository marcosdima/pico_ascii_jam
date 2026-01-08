from .module import Module
from .variants.debug import Debug
from .variants.movement import Movement
from .variants.wasd import WASD
from .variants.background import Background


class Modules(Module):
    ''' Modules container class. '''
    def set_wasd(self, speed: float = 200.0):
        ''' Set WASD module with given speed. '''
        self.wasd = WASD(self.owner)
        self.wasd.speed = speed


    def set_debug(self):
        ''' Set Debug module. '''
        self.debug = Debug(self.owner)


    def set_background(self):
        ''' Set Background module. '''
        self.background = Background(self.owner)


    ''' Module abstract methods. '''
    def setup(self):
        # Set basic modules.
        self.movement = Movement(self.owner)