from ..composed.__composed import Composed
from ..composed.pickaxe import Pickaxe
from ..composed.slingshot import Slingshot
from ..ascii.base.avatar import Avatar
from ...interfaces import Life
from .....types import Color, Resource, MouseButton, ColliderGroup
from .....utils import Resources


class Player(Life, Composed):
    def __init__(self):
        super().__init__()

        # Avatar setup.
        self.avatar = Avatar()
        self.avatar.set_size((125, 125))
        self.avatar.set_color(Color.YELLOW)

        # Resources state.
        self.resources = Resources()
        self.resources.recolect(Resource.ROCK, 10)

        # Tools.
        self.pickaxe = Pickaxe()
        self.slingshot = Slingshot()

        # Add all parts to the composed player
        self.add_part(self.avatar, offset=(0, 0))
        self.add_part(self.pickaxe, offset=(80, -20))
        self.add_part(self.slingshot, offset=(80, -30))

        # Default main tool.
        self.main_tool: Composed = None
        self.switch_tool()

        # Set wasd.
        self.modules.set_wasd()
        self.press_mouse_button.add_callback(self.__on_mouse_button_press)


    def _on_space_change(self, space):
        super()._on_space_change(space)
        
        # Set collider group of pickaxe.
        self.pickaxe.create_collision_shapes_from_parts()
        self.pickaxe.set_collision_type(ColliderGroup.TOOL)

        # Set avatar.
        self.avatar.set_collision_type(ColliderGroup.PLAYER)
        self.avatar.create_own_shape()
        self.avatar.modules.set_debug()

        # Set actions.
        self.modules.events.on_key_E_pressed.add_callback(
            lambda: self.pickaxe.use() if self.pickaxe == self.main_tool else None
        )


    def __on_mouse_button_press(self, mouse_button: MouseButton):
        if mouse_button == MouseButton.RIGHT:
            self.switch_tool()

    
    def switch_tool(self):
        '''Switch between main tools.'''
        if self.main_tool == self.pickaxe:
            self.main_tool = self.slingshot
            self.pickaxe.hide()
        else:
            self.main_tool = self.pickaxe
            self.slingshot.hide()
        self.main_tool.show()


    def set_main_tool(self, tool: Composed):
        '''Set main tool to the given one.'''
        if tool not in (self.pickaxe, self.slingshot):
            raise ValueError("Tool must be either pickaxe or slingshot.")
        self.main_tool.hide()
        self.main_tool = tool
        self.main_tool.show()
