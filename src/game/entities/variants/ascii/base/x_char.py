from ..ascii import Ascii
from ......types import Color, Pixel


class X(Ascii):
	"""X ASCII entity (U+0058).

	Pixelated X using a 3x4 grid per provided path.
	"""

	def get_ascii_unicode(self) -> int:
		return 0x0058  # 'X'

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		# Based on path: top corners, center column (rows 1-2), bottom corners
		return [
			p(0, 0),		p(2, 0),
			        p(1, 1),
			        p(1, 2),
			p(0, 3),		p(2, 3),
		]
