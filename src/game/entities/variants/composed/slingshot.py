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

		unit = 10
		fork = V(unit)      # upper fork
		handle = X(unit)    # handle/cross

		fork.set_color(Color.GRAY)
		handle.set_color(Color.BROWN)

		self.add_part(handle, offset=(0, unit))
		self.add_part(fork, offset=(0, -unit * 2))
