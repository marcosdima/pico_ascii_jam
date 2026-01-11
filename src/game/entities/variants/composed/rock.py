import pymunk


from .__composed import Composed
from ..ascii.base.frame import Frame
from ..ascii.base.parentheses import Parentheses
from ..ascii.base.x_char import X
from ..ascii.base.v_char import V
from .....types import Color, ColliderGroup
from .....utils import CollisionHandler


class Rock(Composed):
    """Composed entity representing a rock.

    Built from a Frame container and three ASCII parts:
    - Parentheses
    - X
    - V
    """

    def __init__(self):
        super().__init__()
        self.frame = Frame()
        self.parentheses = Parentheses()
        self.x_char = X()
        self.v_char = V()
        s = 5
        self.frame.set_size((50 * s, 50 * s))
        self.parentheses.set_size((15 * s, 30 * s))
        self.x_char.set_size((15 * s, 25 * s))
        self.v_char.set_size((15 * s, 25 * s))

        self.frame.set_color(Color.GRAY)
        self.parentheses.set_color(Color.GRAY)
        self.x_char.set_color(Color.GRAY)
        self.v_char.set_color(Color.GRAY)

        # Add frame as base
        self.add_part(self.frame, offset=(0, 0))

        # Add secondary ASCII characters inside the frame
        self.add_part(self.parentheses, offset=(-10, -5))
        self.add_part(self.x_char, offset=(8, -2))
        self.add_part(self.v_char, offset=(0, 10))

        


    def on_space_change(self, space):
        super().on_space_change(space)
        # Set collider group
        self.size = self.frame.size
        self.modules.collision.create_own_shape()
        self.modules.collision.set_collision_type(ColliderGroup.ENVIRONMENT)

        # Set collision handler
        collision_handler = (
            CollisionHandler(ColliderGroup.ENVIRONMENT, ColliderGroup.TOOL)
            .set_begin(self.__on_begin_collision_with_tool)
        )
        self.modules.collision.set_new_handler(collision_handler)



    def __on_begin_collision_with_tool(self, arbiter: pymunk.Arbiter, space: pymunk.Space, data: dict) -> bool:
        print("Rock: Collided with tool!")
        return True
