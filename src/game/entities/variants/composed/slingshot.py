from .__composed import Composed
from ..ascii.base.v_char import V
from ..ascii.base.x_char import X
from .....types import Color


class Slingshot(Composed):
	"""Composed entity representing a slingshot.

	Built from `V` (fork) and `X` (handle cross) parts.
	"""

	def __init__(self):
		super().__init__()

		fork = V()      # upper fork
		handle = X()    # handle/cross

		s = 1
		fork.set_size((30 * s, 40 * s))
		handle.set_size((30 * s, 40 * s))

		fork.set_color(Color.GRAY)
		handle.set_color(Color.BROWN)

		self.add_part(handle, offset=(0, handle.size.y / 2))
		self.add_part(fork, offset=(0, -fork.size.y / 4))

