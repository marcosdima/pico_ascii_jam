import pymunk, math


from .__module import Module


class Follower(Module):
    ''' Follower module. '''
    def setup(self):
        self.__following = True
        self.target: pymunk.Body = None  # Body to follow.
        self.offset = pymunk.Vec2d(0, 0)
        self.follow_angle: bool = True
        self.angle_offset: float = 0.0  # Radians
        self.direct_follow: bool = False  # Flag para modo directo
        self.owner.set_body_type(pymunk.Body.KINEMATIC)


    def _on_owner_update(self, delta_time):
        ''' Called when the owner entity is updated. '''
        if self.has_target() and self.__following:
            # Calculate target position with rotated offset.
            angle = self.target.angle
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            
            rotated_offset_x = self.offset.x * cos_a - self.offset.y * sin_a
            rotated_offset_y = self.offset.x * sin_a + self.offset.y * cos_a
            rotated_offset = pymunk.Vec2d(rotated_offset_x, rotated_offset_y)
            
            target_pos = self.target.position + rotated_offset
            
            if self.direct_follow:
                self.owner.body.position = target_pos
                self.owner.body.velocity = pymunk.Vec2d(0, 0)
            else:
                current_pos = self.owner.body.position
                direction = target_pos - current_pos
                distance = direction.length
                
                if distance > 1:
                    velocity = direction.normalized() * min(distance * 10, 700)
                    self.owner.body.velocity = velocity
                else:
                    self.owner.body.velocity = pymunk.Vec2d(0, 0)
                    self.owner.body.position = target_pos
            
            if self.follow_angle:
                self.owner.body.angle = self.target.angle + self.angle_offset
    
    
    def set_target(
            self,
            body=pymunk.Body,
            offset=(0, 0),
            angle_offset: float = 0.0,
            follow_angle: bool = True,
            direct_follow: bool = False
        ):
        ''' Set Follower module. '''
        self.target = body
        self.offset = pymunk.Vec2d(*offset)
        self.angle_offset = float(angle_offset)
        self.follow_angle = bool(follow_angle)
        self.direct_follow = bool(direct_follow)


    def has_target(self) -> bool:
        ''' Check if there is a target to follow. '''
        return self.target is not None


    def stop_following(self):
        ''' Stop following the target. '''
        if self.has_target():
            self.__following = False


    def start_following(self):
        if self.has_target():
            self.__following = True
