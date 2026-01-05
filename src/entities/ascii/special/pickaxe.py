from ..ascii import Ascii, pygame
from ....core.parasites import Border
from ....core.interfaces import Collider
from ....types import Color


class Pickaxe(Ascii, Collider):
    ''' An ASCII entity that represents a pickaxe character. '''

    ''' Entity overrides. '''
    def get_default_color(self):
        return Color.GREEN


    def get_default_parasites(self):
        return super().get_default_parasites() + [self.collision]


    ''' Entity life cycle overrides. '''
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
