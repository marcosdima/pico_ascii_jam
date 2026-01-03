from ..ascii import Ascii, pygame
from ....core.parasites import Border, Trigger
from ....core.interfaces import Collider
from .pickaxe import Pickaxe


class Rock(Ascii, Collider):
    ''' An ASCII entity that represents a rock character. '''

    ''' Entity life cycle overrides. '''
    def setup(self):
        super().setup()
        self.trigger = Trigger(key='e', action=lambda: print(f'Interacted with {self.name}'))
        self.add_parasite(Border())
        self.add_parasite(self.collision)   


    def update(self, dt):
        super().update(dt)

        # Calculate collision box for pickaxe.
        self.collision_box = self.transform.get_rect()

        # Print collision box for debugging.
        pygame.draw.rect(self.surface, self.color.to_pygame_color(), self.collision_box, 2)


    ''' Collider interface implementation. '''
    def on_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            self.add_parasite(self.trigger)


    def on_end_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            self.remove_parasite(self.trigger)


    def on_keep_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            #print(f'{self.name} is colliding with {other_collider.name}')
            pass


    ''' Ascii overrides. '''
    def get_default_unicode(self) -> int:
        return 0x30ED  # Default character 'ロ'
