import pygame


from .__module import Module
from .....types import Vector2, Position


class WASD(Module):
    ''' A module that allows movement using WASD keys. '''


    ''' Module abstract methods. '''
    def setup(self):
        super().setup()
        self.curr_direction: Vector2 = Vector2()


    ''' Override methods. '''
    def on_owner_update(self, _):
        keys = pygame.key.get_pressed()
        target = self.owner
        movement = target.modules.movement

        direction = Vector2(0, 0)
        if keys[pygame.K_w]: direction += Vector2.UP
        if keys[pygame.K_s]: direction += Vector2.DOWN
        if keys[pygame.K_a]: direction += Vector2.LEFT
        if keys[pygame.K_d]: direction += Vector2.RIGHT

        # If there's no input, don't start movement.
        normalized_direction = direction.normalized()
        if self.curr_direction != normalized_direction:
            self.curr_direction = normalized_direction
            direction = Position.from_tuple(normalized_direction.to_tuple())
            fields = {
                'direction': direction
            }
            movement.change_trajectory(
                kind='linear',
                fields=fields
            )
        
        if direction != Vector2():
            movement.move(force=10)
    
    def on_draw(self):
        pass



    