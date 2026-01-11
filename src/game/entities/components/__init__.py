from .coloreable import Coloreable
from .visible import Visible
from .input import Input
from .drawable import Drawable
from .collision import Collision


class Components(Coloreable, Visible, Input, Drawable, Collision):
    pass


__all__ = [
    "Components",
]