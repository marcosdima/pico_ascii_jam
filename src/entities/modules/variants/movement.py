from ..module import Module
from ....types import Position

class Movement(Module):
    ''' Movement module. '''
    def go_to(
            self,
            direction: tuple[float, float],
            speed: float,
            infinite: bool = False
            ):
        ''' Set movement direction and speed. '''
        # Set movement parameters.
        self.direction = Position(*direction)
        self.speed = speed
        self.distance = (self.owner.get_position() - self.direction).absolute()  
        self.direction = self.direction.normalized()

        # Update flags.
        self.infinite = infinite
        self.moving = True
    

    ''' Module abstract methods. '''
    def setup(self):
        super().setup()

        # Workflow variables.
        self.speed = 1.0 # 1 unit per second.
        self.direction = Position(0, 0)
        self.distance = Position(0, 0)
        self.target = None

        # Flags.
        self.moving = False
        self.infinite = False


    ''' Module lifecycle methods. '''
    def on_owner_update(self, delta_time):
        if not self.moving or (not self.distance.is_positive() and not self.infinite):
            return
        
        # Move owner towards target.
        movement_vector = self.direction * self.speed * delta_time
        self.distance -= movement_vector
        self.owner.transform.position += movement_vector