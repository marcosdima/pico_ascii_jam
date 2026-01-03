import pygame


from ..parasite import Parasite


class WASD(Parasite):
    ''' A parasite that allows movement using WASD keys. '''
    def __init__(self, speed: float = 100):
        super().__init__()
        self.speed = speed


    ''' Override methods. '''
    def on_update(self, delta_time: float):
        keys = pygame.key.get_pressed()
        target = self.target
        speed = self.speed

        if keys[pygame.K_w]:
            target.transform.position.y -= speed * delta_time
        if keys[pygame.K_s]:
            target.transform.position.y += speed * delta_time
        if keys[pygame.K_a]:
            target.transform.position.x -= speed * delta_time
        if keys[pygame.K_d]:
            target.transform.position.x += speed * delta_time

    
    def on_draw(self):
        pass



    