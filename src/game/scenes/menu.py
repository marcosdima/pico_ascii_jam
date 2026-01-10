from .__scene import Scene
from ..entities import Rock, Entity, TextEntity
from ...types import Resource, Color

BUTTON_COLOR = Color.WHEAT.darker(0.5)
BUTTON_ON_HOVER_COLOR = Color.WHEAT

class Menu(Scene):
    '''Menu scene class.'''
    def setup(self):
        super().setup()
        print("created menu")

        # Set a rock.
        rock = Entity()
        rock.modules.set_debug()
        self.add_entity(rock)
        rock.set_transform(size=(200, 200), position=(200, 150))


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