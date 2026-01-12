from .__composed import Composed
from ..ascii.base.parentheses import Parentheses
from ..ascii.base.pipe import Pipe
from .....types import Color


class Pickaxe(Composed):
	"""Composed entity representing a pickaxe (pico).

	Built from a parentheses head and a pipe handle.
	"""

	def __init__(self):
		super().__init__()

		head = Parentheses()
		handle = Pipe()

		s = 1
		head.set_size((20 * s, 50 * s))
		handle.set_size((10 * s, 50 * s))

		head.rotate(-90)

		handle.set_color(Color.BROWN)
		head.set_color(Color.GRAY)

		self.add_part(handle, offset=(0, handle.size.y / 4))
		self.add_part(head, offset=(0, -head.size.y / 4))
