import pygame


from .__module import Module
from .....types import Vector2


class WASD(Module):
    ''' A module that allows movement using WASD keys. '''


    ''' Module abstract methods. '''
    def setup(self):
        super().setup()
        self.curr_direction: Vector2 = Vector2()


    ''' Override methods. '''
    def _on_owner_update(self, _):
        keys = pygame.key.get_pressed()
        body = self.owner.body

        direction = Vector2(0, 0)
        if keys[pygame.K_w]: direction.y -= 1
        if keys[pygame.K_s]: direction.y += 1
        if keys[pygame.K_a]: direction.x -= 1
        if keys[pygame.K_d]: direction.x += 1

        if direction.x != 0 or direction.y != 0:
            direction = direction.normalized()
            speed = 200  # px / segundo
            body.velocity = (direction.x * speed, direction.y * speed)
        else:
            aux_velocity = Vector2(body.velocity.x, body.velocity.y)
            if aux_velocity.magnitude() < 1:
                body.velocity = (0, 0)
            else:   
                body.velocity = (aux_velocity.x * 0.9, aux_velocity.y * 0.8)

    
    def on_draw(self):
        pass



    