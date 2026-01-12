from .__scene import Scene
from ..entities import Rock
from ..entities.variants.special.trigger import Trigger
from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Menu(Scene):
    '''Menu scene class.'''
    def setup(self):
        super().setup()
        
        # Rock in the exact center
        rock = Rock()
        rock.body.position = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.add_entity(rock)
        
        # Test instantiator - create some triggers
        trigger1 = rock.modules.instantiator.create_trigger((WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4))
        trigger1.on_player_enter.add_callback(lambda: print("Player entered trigger 1"))
        self.add_entity(trigger1)

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