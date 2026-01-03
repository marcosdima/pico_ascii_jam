import pygame


from ..parasite import Parasite


class Trigger(Parasite):
    ''' A parasite that triggers an action when the correct key is pressed. '''
    def __init__(self, key:str, action: callable):
        super().__init__()
        self.key = key
        self.action = action
        self.pressed = False

    
    ''' Override methods. '''
    def on_update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[getattr(pygame, f'K_{self.key}').__int__()]:
            self.pressed = True
        else:
            if self.pressed:
                self.action()
            self.pressed = False

    
    def on_draw(self):
        pass