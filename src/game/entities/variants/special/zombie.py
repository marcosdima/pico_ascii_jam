import pymunk
import math

from ..composed.__composed import Composed
from ..ascii.base.avatar import Avatar
from ..special.player import Player
from ...interfaces import Life
from .....types import Color, ColliderGroup

DAMAGE = 25.0

class Zombie(Life, Composed):
    def __init__(self):
        super().__init__()

        # Avatar setup.
        self.avatar = Avatar()
        self.avatar.set_ascii_size(20)
        self.avatar.set_color(Color.GREEN)


        # Add all parts to the composed player
        self.add_part(self.avatar, offset=(0, 0))

        # Chase behavior state
        self.__max_speed: float = 400.0
        self.__acceleration: float = 600.0
        self.__drag: float = 0.9
        self.__player_contact = None  # Track player currently colliding
        self.__avoid_timer: float = 0.0
        self.__avoid_dir: pymunk.Vec2d | None = None

        # Movement update
        self.update.add_callback(self.__on_update)

        # Attack cooldown (copy of pickaxe style)
        self.recharge_time = 1.0
        self._recharge_timer = 0.0
        self.update.add_callback(self._update_recharge)
        
        # Stun after attack
        self.__attack_stun_timer = 0.0
        self.__attack_stun_duration = 0.8  # Duration after attacking before pursuing again
        

    def _on_space_change(self, space):
        super()._on_space_change(space)
        
        self.set_collision_type(ColliderGroup.ENEMY)
        self.set_body_type('dynamic')
        self.size = self.avatar.size
        self.size.x += 0.8
        self.body.mass = 6.0
        self.body.moment = pymunk.moment_for_box(self.body.mass, (self.size.x, self.size.y))
        self.create_own_shape()
        for shape in self.body.shapes:
            shape.friction = 1.0
            shape.elasticity = 0.05
        self.body.angular_velocity = 0
        self.body.angular_velocity_limit = 0
        self.body.velocity_func = lambda body, gravity, damping, dt: pymunk.Body.update_velocity(body, gravity, 0.98, dt)
        self.modules.set_debug()

        # Damage player on physical collision
        from .....utils import CollisionHandler
        handler = (
            CollisionHandler(ColliderGroup.ENEMY, ColliderGroup.PLAYER)
                .set_begin(self.__on_begin_collision_with_player)
                .set_separate(self.__on_end_collision_with_player)
        )
        self.set_new_handler(handler)

        # Bounce off rocks and keep chasing
        handler_rock = (
            CollisionHandler(ColliderGroup.ENEMY, ColliderGroup.RESOURCE)
                .set_begin(self.__on_collision_with_rock)
        )
        self.set_new_handler(handler_rock)

        # Ignore collision with tools
        handler_tool = (
            CollisionHandler(ColliderGroup.ENEMY, ColliderGroup.TOOL)
                .set_begin(lambda *args: False)  # Return False to prevent collision
        )
        self.set_new_handler(handler_tool)


    def __on_update(self, dt: float):
        # Update attack stun timer
        if self.__attack_stun_timer > 0:
            self.__attack_stun_timer -= dt
            self.body.velocity *= 0.6
            self.body.angular_velocity = 0
            return
        
        # If still in contact and cooldown is over, keep attacking periodically
        if self.__player_contact is not None and self.charged():
            self.__attack_player(self.__player_contact)

        player = Player.get_instance()
        if player is None:
            self.body.velocity *= self.__drag
            self.body.angular_velocity = 0
            return

        # Rotate to face player
        player_dir = player.body.position - self.body.position
        if player_dir.length > 0:
            angle = math.atan2(player_dir.y, player_dir.x)
            # Prevent upside down: if angle points downward, flip 180 degrees
            if angle > math.pi / 2 or angle < -math.pi / 2:
                angle += math.pi if angle > 0 else -math.pi
            self.body.angle = angle

        # Choose direction: avoid rock briefly, else chase player
        if self.__avoid_timer > 0 and self.__avoid_dir is not None:
            self.__avoid_timer -= dt
            direction = self.__avoid_dir
        else:
            direction = player.body.position - self.body.position
            if direction.length > 0:
                direction = direction.normalized()
            else:
                direction = pymunk.Vec2d(0, 0)
            self.__avoid_dir = None
            self.__avoid_timer = 0

        desired = direction * self.__max_speed
        vel = self.body.velocity
        steering = desired - vel
        max_steer = self.__acceleration * dt
        if steering.length > max_steer:
            steering = steering.normalized() * max_steer

        new_vel = vel + steering
        if new_vel.length > self.__max_speed:
            new_vel = new_vel.normalized() * self.__max_speed

        self.body.velocity = new_vel
        self.body.angular_velocity = 0


    def _update_recharge(self, dt: float):
        """Update recharge timer to avoid constant attacks."""
        if self._recharge_timer > 0:
            self._recharge_timer -= dt
            if self._recharge_timer < 0:
                self._recharge_timer = 0


    def charged(self) -> bool:
        """Check if zombie can attack."""
        return self._recharge_timer == 0


    def __on_begin_collision_with_player(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict) -> bool:
        # Damage player on contact
        shape_a, shape_b = arbiter.shapes
        other = shape_b if shape_a.body is self.body else shape_a
        player = getattr(other, 'entity', None)
        if player:
            self.__player_contact = player
            if self.charged():
                self.__attack_player(player)
        return True


    def __on_end_collision_with_player(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict):
        # Clear contact when separation happens
        self.__player_contact = None


    def __on_collision_with_rock(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict) -> bool:
        shape_a, shape_b = arbiter.shapes
        other = shape_b if shape_a.body is self.body else shape_a
        away = self.body.position - other.body.position if hasattr(other, 'body') else pymunk.Vec2d(0, 0)
        if away.length > 0:
            away = away.normalized()
            self.__avoid_dir = away
            self.__avoid_timer = 0.35
            self.body.velocity = away * (self.__max_speed * 0.6)
        self.body.angular_velocity = 0
        return True


    def __attack_player(self, player):
        # Create a short-lived damage trigger centered on zombie
        center = (self.body.position.x, self.body.position.y)
        self.modules.instantiator.create_damage_trigger(
            size=(150, 150),
            offset=center,
            damage=DAMAGE,
            lifetime=0.15,
            knockback=420.0,
        )
        # Start cooldown
        self._recharge_timer = self.recharge_time
        
        # Stun after attack: don't pursue for a moment
        self.__attack_stun_timer = self.__attack_stun_duration
        self.__avoid_timer = 0
        self.__avoid_dir = None
