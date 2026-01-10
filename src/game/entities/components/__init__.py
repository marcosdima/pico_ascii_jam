from .coloreable import Coloreable
from .visible import Visible
from .familiar import Familiar
from .input import Input
from .collider import Collider
from .drawable import Drawable


class Components(Coloreable, Visible, Familiar, Input, Collider, Drawable):
    pass


__all__ = [
    "Components",
]