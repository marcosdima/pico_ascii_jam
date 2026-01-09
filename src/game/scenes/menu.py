from .__scene import Scene
from ...entities import Rock, Sign, Entity
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
        sign = self.__create_sign(
            text='Start',
            follow=rock,
            anchor=Anchor.BOTTOM_CENTER,
            offset=15.0,
        )
        sign.set_transform(size=(200, 100), position=(400, 150))
        

    def __create_sign(
        self,
        text: str,
        follow: 'Entity',
        anchor: Anchor = Anchor.CENTER,
        offset: float = 10.0,
    ) -> Sign:
        '''Create a sign entity.'''
        sign = Sign(text=text, anchor=anchor, follow=follow, offset=offset)
        sign.set_color(BUTTON_COLOR)
        self.add_entity(sign)
        follow.mouse_on.add_callback(lambda sg=sign: sg.set_color(BUTTON_ON_HOVER_COLOR))
        follow.mouse_exit.add_callback(lambda sg=sign: sg.set_color(BUTTON_COLOR))
        return sign