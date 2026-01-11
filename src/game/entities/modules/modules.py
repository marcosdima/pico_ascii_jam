from typing import Literal, TypeAlias


from .variants.__module import Module
from .variants.debug import Debug
from .variants.movement import Movement
from .variants.wasd import WASD
from .variants.background import Background
from .variants.layouts.__layout import Layout
from .variants.layouts.grid import Grid


LayoutType: TypeAlias = Literal['grid']


class Modules(Module):
    ''' Modules container class. '''
    def set_wasd(self):
        ''' Set WASD module with given speed. '''
        self.wasd = WASD(self.owner)


    def set_debug(self):
        ''' Set Debug module. '''
        self.debug = Debug(self.owner)


    def set_background(self):
        ''' Set Background module. '''
        self.background = Background(self.owner)

    
    def set_layout(self, layout_type: LayoutType, config: dict = {}):
        ''' Set layout module of given type. '''
        layout: Layout = None
        if layout_type == 'grid':
            layout = Grid(self.owner)
        else:
            raise ValueError(f"Unknown layout type: {layout_type}")

        layout.set_settings(config)
        self.layout = layout


    ''' Module abstract methods. '''
    def setup(self):
        # Set basic modules.
        self.movement = Movement(self.owner)