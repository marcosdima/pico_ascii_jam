from .base import Base
from .variants.coloreable import Coloreable
from .variants.visible import Visible
from .variants.familiar import Familiar
from .variants.input import Input


class JointInterface(Coloreable, Visible, Familiar, Input):
    pass


__all__ = [
    "Base",
    "Coloreable",
    "Visible",
    "JointInterface",
]