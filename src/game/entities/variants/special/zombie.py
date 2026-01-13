from ..composed.__composed import Composed
from ..ascii.base.avatar import Avatar
from ...interfaces import Life
from .....types import Color, ColliderGroup
import pymunk

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
        self.__chase_target: pymunk.Vec2d | None = None
        self.__chase_speed: float = 260.0
        self.__pulse_interval: float = 1.5
        self.__pulse_timer: float = 0.0
        self.__player_contact = None  # Track player currently colliding

        # Movement update
        self.update.add_callback(self.__on_update)

        # Attack cooldown (copy of pickaxe style)
        self.recharge_time = 1.0
        self._recharge_timer = 0.0
        self.update.add_callback(self._update_recharge)


    def _on_space_change(self, space):
        super()._on_space_change(space)
        
        self.set_collision_type(ColliderGroup.ENEMY)
        self.size = self.avatar.size
        self.size.x += 0.8
        self.create_own_shape()
        self.modules.set_debug()

        # Damage player on physical collision
        from .....utils import CollisionHandler
        handler = (
            CollisionHandler(ColliderGroup.ENEMY, ColliderGroup.PLAYER)
                .set_begin(self.__on_begin_collision_with_player)
                .set_separate(self.__on_end_collision_with_player)
        )
        self.set_new_handler(handler)


    def __on_update(self, dt: float):
        # Simple chase movement towards last detected player position
        # Pulse timer for periodic scans
        self.__pulse_timer += dt
        if self.__pulse_timer >= self.__pulse_interval:
            self.__pulse_timer = 0.0
            self.__pulse_scan()

        # If still in contact and cooldown is over, keep attacking periodically
        if self.__player_contact is not None and self.charged():
            self.__attack_player(self.__player_contact)

        if self.__chase_target is None:
            self.body.velocity = pymunk.Vec2d(0, 0)
            return

        current = self.body.position
        direction = self.__chase_target - current
        dist = direction.length
        if dist < 5:
            # Small deadzone: move slowly to avoid jitter
            self.body.velocity = direction.normalized() * (self.__chase_speed * 0.35)
            return

        self.body.velocity = direction.normalized() * self.__chase_speed


    def _update_recharge(self, dt: float):
        """Update recharge timer to avoid constant attacks."""
        if self._recharge_timer > 0:
            self._recharge_timer -= dt
            if self._recharge_timer < 0:
                self._recharge_timer = 0


    def charged(self) -> bool:
        """Check if zombie can attack."""
        return self._recharge_timer == 0


    def __pulse_scan(self):
        # Create a large trigger centered at zombie to detect player
        size = (1000, 1000)
        center = (self.body.position.x, self.body.position.y)
        trigger = self.modules.instantiator.create_trigger(size=size, offset=center)

        # When player enters, update chase target to current player position
        def on_player(player):
            pos = pymunk.Vec2d(player.body.position.x, player.body.position.y)
            self.__chase_target = pos
            return True
        trigger.on_player_enter = on_player


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
