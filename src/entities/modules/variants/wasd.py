import pygame


from ..module import Module
from ....types import Vector2


class WASD(Module):
    ''' A module that allows movement using WASD keys. '''


    ''' Module abstract methods. '''
    def setup(self):
        super().setup()
        self.speed: float = 200.0


    ''' Override methods. '''
    def on_owner_update(self, delta_time: float):
        keys = pygame.key.get_pressed()
        target = self.owner
        speed = self.speed

        direction = Vector2(0, 0)
        if keys[pygame.K_w]: direction += Vector2.UP
        if keys[pygame.K_s]: direction += Vector2.DOWN
        if keys[pygame.K_a]: direction += Vector2.LEFT
        if keys[pygame.K_d]: direction += Vector2.RIGHT

        target.modules.movement.go_to(
            direction=direction.normalized().to_tuple(),
            speed=speed,
            infinite=True
        )
    
    def on_draw(self):
        pass



    