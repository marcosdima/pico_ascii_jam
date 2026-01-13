import pymunk
from typing import TYPE_CHECKING


from .__composed import Composed
from ..ascii.base.frame import Frame
from ..ascii.base.ke_char import Ke
from ..ascii.base.me_char import Me
from ..ascii.base.x_char import X
from ..ascii.base.v_char import V
from ...interfaces import Life
from .....types import ColliderGroup, Resource
from .....utils import CollisionHandler, AudioManager


class Rock(Life, Composed):
    """Composed entity representing a rock.

    Built from a Frame container and three ASCII parts:
    - Ke (゜)
    - Me (メ)
    - V
    """

    def __init__(self, resource: Resource = Resource.ROCK):
        super().__init__()

        self.resource = resource
        self.collision_type = ColliderGroup.RESOURCE.value

        # Create ASCII parts.
        unit = 15
        self.frame = Frame(ascii_size=35)
        self.phase_1 = Ke(ascii_size=unit)
        self.phase_2 = Me(ascii_size=unit)
        self.phase_2.rotate(180)

        self.frame.set_color(resource.get_color())
        self.phase_1.set_color(resource.get_color())
        self.phase_2.set_color(resource.get_color())
        
        # Add frame as base
        self.add_part(self.frame, offset=(0, 0))

        # Add secondary ASCII characters inside the frame
        self.add_part(self.phase_1, offset=(-unit, unit / 2))
        self.add_part(self.phase_2, offset=(0, 0))

        # Hide parts initially
        self.__show_part: Ke | Me | V | None = None
        self.phase_1.hide()
        self.phase_2.hide()

        # Health state
        self.set_max_health(resource.value)
        self.on_death.add_callback(self.free)
        self.on_damage_received.add_callback(self.__on_damage_received)


    ''' Override. '''
    def free(self):
        # Drop resource item.
        self.modules.instantiator.create_drop(
            of=self.resource,
            offset=self.body.position,
            timeout=10,
        )
        super().free()


    def _on_space_change(self, space):
        super()._on_space_change(space)

        # Set collider group
        self.size = self.frame.size
        self.create_own_shape()
        self.modules.set_debug()


        # Set collision handler
        collision_handler = (
            CollisionHandler(ColliderGroup.RESOURCE, ColliderGroup.AREA)
                .set_begin(self.__on_begin_collision_with_tool)
        )
        self.set_new_handler(collision_handler)


    def __on_damage_received(self, _: float):
        # Change visible part based on current health
        health_ratio = self.current_health / self.max_health
        if health_ratio < 0.6:
            self._turn_part_visible(self.phase_2)
        elif health_ratio < 0.9:
            self._turn_part_visible(self.phase_1)


    def __on_begin_collision_with_tool(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict) -> bool:
        # Identify the other shape/entity (the tool) in this collision
        shape_a, shape_b = arbiter.shapes
        other_shape = shape_b if shape_a.body is self.body else shape_a
        tool = getattr(other_shape, 'entity', None)
        
        if tool and hasattr(tool, 'damage'):
            damage = tool.damage
            self.damage(damage)
            
            # Play hit sound
            audio = AudioManager.get_instance()
            audio.play_hit_rock()
            
            print('Life remaining:', self.current_health)

        return True
    

    def _turn_part_visible(self, part):
        if self.__show_part is not None:
            self.__show_part.hide()
        self.__show_part = part
        self.__show_part.show()
        
        
