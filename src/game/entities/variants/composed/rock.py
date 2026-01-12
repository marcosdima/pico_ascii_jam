import pymunk


from .__composed import Composed
from ..ascii.base.frame import Frame
from ..ascii.base.parentheses import Parentheses
from ..ascii.base.x_char import X
from ..ascii.base.v_char import V
from ...interfaces import Life
from .....types import ColliderGroup, Resource
from .....utils import CollisionHandler


class Rock(Life, Composed):
    """Composed entity representing a rock.

    Built from a Frame container and three ASCII parts:
    - Parentheses
    - X
    - V
    """

    def __init__(self, resource: Resource = Resource.ROCK):
        super().__init__()

        self.resource = resource
        self.collision_type = ColliderGroup.RESOURCE.value

        # Create ASCII parts.
        self.frame = Frame()
        self.parentheses = Parentheses()
        self.x_char = X()
        self.v_char = V()
        s = 5
        self.frame.set_size((50 * s, 50 * s))
        self.parentheses.set_size((15 * s, 30 * s))
        self.x_char.set_size((15 * s, 25 * s))
        self.v_char.set_size((15 * s, 25 * s))

        self.frame.set_color(resource.get_color())
        self.parentheses.set_color(resource.get_color())
        self.x_char.set_color(resource.get_color())
        self.v_char.set_color(resource.get_color())
        
        # Add frame as base
        self.add_part(self.frame, offset=(0, 0))

        # Add secondary ASCII characters inside the frame
        self.add_part(self.parentheses, offset=(-10, -5))
        self.add_part(self.x_char, offset=(8, -2))
        self.add_part(self.v_char, offset=(0, 10))

        # Hide parts initially
        self.parentheses.hide()
        self.x_char.hide()
        self.v_char.hide()

        # Health state
        self.set_max_health(resource.value)
        self.on_death.add_callback(self.free)


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


    def __on_begin_collision_with_tool(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict) -> bool:
        # Identify the other shape/entity (the tool) in this collision
        shape_a, shape_b = arbiter.shapes
        other_shape = shape_b if shape_a.body is self.body else shape_a
        tool = getattr(other_shape, 'entity', None)
        
        if tool and hasattr(tool, 'damage'):
            damage = tool.damage
            self.damage(damage)
            print('Life remaining:', self.current_health)

        return True
    
