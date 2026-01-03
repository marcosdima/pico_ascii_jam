import pygame


from ...config import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_COLOR, FONT_PATH
from .__scene import Scene, Entity
from ...core.parasites import Border

class MenuScene(Scene):
    '''Main menu scene that displays "Hello World"'''


    ''' Scene abstract methods. '''
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print('click en', x, y)

    
    def cleanup(self):
        pass


    def load_resources(self):
        entity = Entity(surface=self.surface)
        entity.transform.set_scale(100, 100)
        entity.add_parasite(Border())
        self.add_child(entity)