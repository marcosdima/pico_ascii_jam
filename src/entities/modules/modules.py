from .module import Module
from .variants.family import Family
from .variants.debug import Debug


class Modules(Module):
    ''' Modules container class. '''
    
    
    ''' Module abstract methods. '''
    def setup(self):
        self.family: Family = Family(self.owner)
        self.debug: Debug = Debug(self.owner)