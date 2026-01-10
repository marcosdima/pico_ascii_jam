from .__scene import Scene
from ...entities import Rock, Entity, TextEntity
from ...types import Resource, Anchor, Color

BUTTON_COLOR = Color.WHEAT.darker(0.5)
BUTTON_ON_HOVER_COLOR = Color.WHEAT

class Menu(Scene):
    '''Menu scene class.'''
    def __init__(self):
        super().__init__()

        # Set a rock.
        rock = Rock(resource=Resource.ROCK)
        self.add_entity(rock)
        rock.set_transform(size=(200, 200), position=(200, 150))

        # Set a sign.
        self.sign: TextEntity = self.__create_sign(text='Start', follow=rock)

        
    def __create_sign(
        self,
        follow: Entity,
        text: str,
    ) -> TextEntity:
        '''Create a sign entity.'''
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
        return sign