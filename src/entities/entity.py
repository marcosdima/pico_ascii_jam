from typing import TYPE_CHECKING 
from abc import ABC


from ..types import Transform, Color
from ..core.interfaces import Coloreable, ImmuneSystem
from ..core.parasites import Parasite


if TYPE_CHECKING:
    from ..core.scenes import Scene


class Entity(Coloreable, ImmuneSystem, ABC):
    __count = 0


    def set_transform(
            self,
            position: tuple[float, float] = None,
            size: tuple[float, float] = None,
            scale: tuple[float, float] = None,
            z_index: int = None,
        ):
        '''Set the entity's transform.'''
        if position is not None:
            self.transform.set_position(*position)
        if size is not None:
            self.transform.set_size(*size)
        if scale is not None:
            self.transform.set_scale(*scale)
        if z_index is not None:
            self.transform.z_index = z_index
        return self


    def __set_default_parasites(self):
        '''Set the default parasites for the entity.'''
        for parasite in self.get_default_parasites():
            self.add_parasite(parasite)


    ''' Visibility methods. '''
    def show(self):
        '''Make the entity visible.'''
        self.__show = True
        return self
    

    def hide(self):
        '''Make the entity invisible.'''
        self.__show = False
        return self


    def is_visible(self) -> bool:
        '''Check if the entity is visible.'''
        return self.__show
    

    ''' Overrides. '''
    def get_default_color(self):
        return Color.WHITE


    def get_default_parasites(self) -> list[Parasite]:
        return []


    ''' Life cycle. '''
    def setup(self):
        self.__set_default_parasites()
        

    def update(self, dt):
        self.handle_update(dt)


    def draw(self) -> bool:
        if self.__show:
            self.handle_draw()
        return self.__show


    ''' Python special methods. '''
    def __init__(self, scene: 'Scene'):
        super().__init__()
        self.scene = scene
        self.surface = scene.game.screen
        
        # Set default values.
        self.transform = Transform()
        self.__show = True
        self.color = self.get_default_color()

        # Set an unique name.
        self.name = f'Entity_{Entity.__count}'
        Entity.__count += 1

        # Call setup method.
        self.setup()


    def __str__(self):
        return f'<Entity name={self.name} transform={self.transform} color={self.get_color()}>'
