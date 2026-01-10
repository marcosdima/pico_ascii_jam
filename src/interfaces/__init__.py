from .base import Base
from .variants.coloreable import Coloreable
from .variants.visible import Visible
from .variants.familiar import Familiar
from .variants.input import Input
from .variants.collider import Collider
from .variants.drawable import Drawable


class JointInterface(Coloreable, Visible, Familiar, Input, Collider, Drawable):
    pass


__all__ = [
    "Base",
    "Coloreable",
    "Visible",
    "JointInterface",
    "Familiar",
    "Input",
    "Collider",
]