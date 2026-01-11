import pymunk


from .__module import Module


class Follower(Module):
    ''' Follower module. '''
    def setup(self):
        self.target: pymunk.Body = None  # Body to follow.
        self.offset = pymunk.Vec2d(0, 0)
        self.owner.set_body_type(pymunk.Body.KINEMATIC)


    def _on_owner_update(self, delta_time):
        ''' Called when the owner entity is updated. '''
        if self.target:
            # Rotate offset according to target's angle
            import math
            angle = self.target.angle
            cos_a = math.cos(angle)
            sin_a = math.sin(angle)
            
            # Rotate the offset vector
            rotated_offset_x = self.offset.x * cos_a - self.offset.y * sin_a
            rotated_offset_y = self.offset.x * sin_a + self.offset.y * cos_a
            rotated_offset = pymunk.Vec2d(rotated_offset_x, rotated_offset_y)
            
            new_pos = self.target.position + rotated_offset
            self.owner.body.position = new_pos
            self.owner.body.angle = self.target.angle
    
    def set_target(self, body=pymunk.Body, offset=(0, 0)):
        ''' Set Follower module. '''
        self.target = body
        self.offset = pymunk.Vec2d(*offset)