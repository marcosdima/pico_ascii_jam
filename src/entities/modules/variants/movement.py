from ..module import Module
from ....types import Position
from ....types.trajectory import Trajectory, TrajectoryType, Fields


class Movement(Module):
    ''' Movement module. '''
    def move(self, force: float):
        '''Start moving in a given direction with a given speed.'''
        self.__moving = True
        self.acc_force += force


    def change_trajectory(self, kind: TrajectoryType, fields: Fields):
        '''Change the current trajectory type and fields.'''
        self.trajectory.set(
            kind=kind,
            start=self.owner.transform.position,
            fields=fields
        )


    ''' Module abstract methods. '''
    def setup(self):
        super().setup()

        self.acc_force = 0.0
        self.speed = 250.0
        self.trajectory = Trajectory()

        # Flags.
        self.__moving = False


    ''' Module lifecycle methods. '''
    def on_owner_update(self, delta_time):
        if not self.__moving:
            return
        elif self.acc_force < 1:
            self.__moving = False
            self.acc_force = 0.0
            return
        
        speed = self.speed
        force = self.acc_force

        if force > speed:
            movement = delta_time * speed
            self.acc_force -= 10 * movement
        else:
            movement = delta_time * force
            self.acc_force -= movement

        next_position = self.trajectory(movement)
        self.owner.transform.position = next_position