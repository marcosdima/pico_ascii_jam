import pymunk


from .__scene import Scene
from ...types import ColliderGroup, Color
from ...utils import CollisionHandler
from ..entities import (
    Entity,
    Parentheses,
    Pipe,
    V,
    Avatar,
    Frame,
)


BUTTON_COLOR = Color.WHEAT.darker(0.5)
BUTTON_ON_HOVER_COLOR = Color.WHEAT


# ASCII scale factor
ASCII_SCALE = 0.5


class Menu(Scene):
    '''Menu scene class.'''
    def setup(self):
        super().setup()

        # Base.
        base = Entity()
        base.body.position = (200, 150)
        base.set_size((100, 100))
        base.set_color(Color.GRAY)
        base.modules.set_wasd()
        self.add_entity(base)
        
        # Second entity.
        second = Entity()
        second.set_size((50, 50))
        second.set_color(Color.BLUE)
        second.body.position = (400, 150)
        second.modules.set_background()
        self.add_entity(second)
        second.modules.follower.set_target(body=base.body, offset=(110, 110))

        # Third entity.
        third = Entity()
        third.set_body_type('static')
        third.set_size((30, 30))
        third.set_color(Color.RED)
        third.body.position = (100, 150)
        third.modules.set_background()
        self.add_entity(third)

        # Collision logic.
        base.modules.collision.set_collision_type(ColliderGroup.PLAYER)
        base.modules.collision.create_own_shape()   
        third.modules.collision.set_collision_type(ColliderGroup.ENEMY)
        third.modules.collision.create_own_shape()
        collision_handler = (
            CollisionHandler(ColliderGroup.PLAYER, ColliderGroup.ENEMY)
            .set_begin(lambda arbiter, space, data: print("Collision began!") or True)
            .set_separate(lambda arbiter, space, data: print("Collision ended!") or None)
        )
        third.modules.collision.set_new_handler(collision_handler)

        # Fourth entity (ASCII target - Parentheses).
        target = Parentheses()
        target.body.position = (10, 150)
        target.set_size((100 * ASCII_SCALE, 250 * ASCII_SCALE))
        target.rotate(-90)
        target.set_color(Color.CYAN)
        self.add_entity(target)
        
        # ASCII tests - Pipe
        pipe = Pipe()
        pipe.body.position = (160, 150)
        pipe.set_size((50 * ASCII_SCALE, 250 * ASCII_SCALE))
        pipe.set_color(Color.YELLOW)
        self.add_entity(pipe)

        
        # ASCII tests - V
        v_char = V()
        v_char.body.position = (460, 150)
        v_char.set_size((20 * ASCII_SCALE * 10, 40 * ASCII_SCALE * 10))
        v_char.set_color(Color.PURPLE)
        self.add_entity(v_char)
        
        # ASCII tests - Avatar
        avatar = Avatar()
        avatar.body.position = (610, 150)
        avatar.set_size((100 * ASCII_SCALE * 2, 100 * ASCII_SCALE * 2))
        avatar.set_color(Color.ORANGE)
        self.add_entity(avatar)
        
        # ASCII tests - Frame
        frame = Frame()
        frame.body.position = (760, 150)
        frame.set_size((100 * ASCII_SCALE, 100 * ASCII_SCALE))
        frame.set_color(Color.CYAN)
        self.add_entity(frame)
        

    '''def __create_sign(
        self,
        follow: Entity,
        text: str,
    ) -> TextEntity:
        sign: TextEntity = TextEntity(text=text, font_size=32)
        sign.set_color(BUTTON_COLOR)
        follow.add_child(sign)

        follow_size = follow.transform.size
        sign_size = sign.transform.size
        rest = follow_size.x - sign_size.x

        sign.set_transform(
            position=(rest / 2, follow_size.y + 20),
        )

        follow.mouse_on.add_callback(lambda sg=sign: sg.set_color(BUTTON_ON_HOVER_COLOR))
        follow.mouse_exit.add_callback(lambda sg=sign: sg.set_color(BUTTON_COLOR))
        return sign'''