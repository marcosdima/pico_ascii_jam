import pymunk
from .__scene import Scene
from ..entities import Entity
from ...types import Resource, Color

BUTTON_COLOR = Color.WHEAT.darker(0.5)
BUTTON_ON_HOVER_COLOR = Color.WHEAT

class Menu(Scene):
    '''Menu scene class.'''
    def setup(self):
        super().setup()

        # Base.
        base = Entity()
        #base.body.position = (200, 150)
        base.modules.set_background()

        base.set_size((100, 100))
        base.set_color(Color.GRAY)
        base.set_body_type(pymunk.Body.DYNAMIC)

        self.add_entity(base)
        base.add_shape_owner(base)


        # Set a rock.
        rock = Entity()
        rock.set_body_type(pymunk.Body.KINEMATIC)
        rock.body.position = (250, 150)
        rock.set_size((100, 100))
        rock.set_color(Color.BROWN)
        
        base.add_child(rock)
        rock.add_shape_owner(rock)

        rock.modules.set_background()
        rock.update.add_callback(lambda _: print(rock.body.position))
        
        base.body.velocity = (50, 50)
        base.body.angle = 90
              
        #base.add_child(rock)
        #print(rock)

        #rock.draw.add_callback(lambda: (rock.body.shapes))
        #rock.set_transform(size=(200, 200), position=(200, 150))


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