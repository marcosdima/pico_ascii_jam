from pygame import Rect


from ..parasite import Parasite


class Collision(Parasite):
    ''' Collision detection parasite. '''
    __register: dict[int, 'Collision'] = {}


    def check_collision(self, other: 'Collision') -> bool:
        rect1 = self.target.transform.get_rect()
        rect2 = other.target.transform.get_rect()
        return rect1.colliderect(rect2)


    ''' Override methods. '''
    def on_draw(self):
        pass


    def on_update(self, delta_time):
        for other in Collision.__register.values():
            if other.id == self.id:
                continue

            if self.check_collision(other):
                if other not in self.in_collision:
                    self.in_collision.append(other)
                    self.on_collision_callback(other.target)
                else:
                    self.on_keep_collision_callback(other.target)
            else:
                if other in self.in_collision:
                    self.in_collision.remove(other)
                    self.on_end_collision_callback(other.target)
                


    ''' Python special methods. '''
    def __init__(
            self,
            on_collision_callback=callable,
            on_keep_collision_callback=callable,
            on_end_collision_callback=callable
        ):
        super().__init__()
        Collision.__register[self.id] = self
        self.in_collision: list['Collision'] = []

        # Callbacks.
        self.on_collision_callback = on_collision_callback
        self.on_keep_collision_callback = on_keep_collision_callback
        self.on_end_collision_callback = on_end_collision_callback