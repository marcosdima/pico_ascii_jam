import pymunk
from typing import Literal, TypeAlias


from .variants.__module import Module
from .variants.debug import Debug
from .variants.wasd import WASD
from .variants.background import Background
from .variants.layouts.__layout import Layout
from .variants.layouts.grid import Grid
from .variants.follower import Follower
from .variants.instantiator import Instantiator
from .variants.events import Events


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

    
    def set_layout(self, layout_type: Literal['grid'], config: dict = {}):
        ''' Set layout module of given type. '''
        layout: Layout = None
        if layout_type == 'grid':
            layout = Grid(self.owner)
        else:
            raise ValueError(f"Unknown layout type: {layout_type}")

        layout.set_settings(config)
        self.layout = layout


    def setup(self):
        '''Set Follower module.'''
        self.follower = Follower(self.owner)
        self.instantiator = Instantiator(self.owner)
        self.events = Events(self.owner)
