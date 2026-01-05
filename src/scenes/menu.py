import pygame


from ...config import WINDOW_WIDTH, WINDOW_HEIGHT, TEXT_COLOR, FONT_PATH
from .__scene import Scene
from ...entities import Avatar, Rock, Gold
from ...core.parasites import WASD


class MenuScene(Scene):
    '''Main menu scene that displays "Hello World"'''


    ''' Scene abstract methods. '''
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            print('click en', x, y)

    
    def cleanup(self):
        pass


    def load_resources(self):
        # Avatar.
        avatar = Avatar(scene=self)
        avatar.set_transform(scale=(8, 8), position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        avatar.add_parasite(WASD(400))

        # Random rock.
        rock = Rock(scene=self)
        rock.set_transform(position=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))

        # Rock gold.
        gold = Gold(scene=self)
        gold.set_transform(
            position=(
                WINDOW_WIDTH // 2 + gold.transform.get_scaled_size().x,
                WINDOW_HEIGHT // 2,
            )
        )

        return [
            avatar,
            rock,
            gold,
        ]
        