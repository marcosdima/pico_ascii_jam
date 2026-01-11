from .coloreable import Coloreable
from .visible import Visible
from .input import Input
from .drawable import Drawable


class Components(Coloreable, Visible, Input, Drawable):
    pass


__all__ = [
    "Components",
]