from ..parasites import Parasite

class ImmuneSystem:
    '''Interface for immune system implementations'''
    def __init__(self):
        super().__init__()
        self.parasites: list[Parasite] = []
        
    
    def add_parasite(self, parasite: Parasite):
        '''Add a parasite to the immune system'''
        self.parasites.append(parasite)
        parasite.set_target(self)


    def remove_parasite(self, parasite: Parasite):
        '''Remove a parasite from the immune system'''
        if parasite in self.parasites:
            self.parasites.remove(parasite)

    
    def handle_update(self, delta_time: float):
        '''Update all parasites in the immune system'''
        for parasite in self.parasites:
            parasite.on_update(delta_time)

    
    def handle_draw(self):
        '''Draw all parasites in the immune system'''
        #print(f'On draw from immune system: {self.parasites}')
        for parasite in self.parasites:
            parasite.on_draw()

    
