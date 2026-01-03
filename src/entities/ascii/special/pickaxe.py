from ..ascii import Ascii, pygame
from ....core.parasites import Border, Collision
from ....core.interfaces import Collider


class Pickaxe(Ascii, Collider):
    ''' An ASCII entity that represents a pickaxe character. '''

    ''' Entity life cycle overrides. '''
    def setup(self):
        super().setup()
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
            print(f'{self.name} collided with {other_collider.name}')


    def on_end_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            print(f'{self.name} ended collision with {other_collider.name}')


    def on_keep_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            print(f'{self.name} is colliding with {other_collider.name}')


    ''' Ascii overrides. '''
    def get_default_unicode(self) -> int:
        return 0x30E4  # Default character 'ヤ'
