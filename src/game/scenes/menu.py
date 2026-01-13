from .__scene import Scene
from ..entities import Rock, Zombie
from config import WINDOW_WIDTH, WINDOW_HEIGHT


class Menu(Scene):
    '''Menu scene class.'''
    def setup(self):
        super().setup()
        
        # Rock in the exact center
        self.rock = Rock()
        self.rock.body.position = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.add_entity(self.rock)

        # Spawn a zombie near the center
        self.zombie = Zombie()
        self.zombie.body.position = (WINDOW_WIDTH / 2 + 200, WINDOW_HEIGHT / 2)
        self.add_entity(self.zombie)


    def test_trigger(self):
        # Test instantiator - create some triggers
        trigger1 = self.rock.modules.instantiator.create_trigger((WINDOW_WIDTH / 4, WINDOW_HEIGHT / 4), (100, 100))
        trigger1.on_player_enter.add_callback(lambda: print("Player entered trigger 1"))
        self.add_entity(trigger1)
