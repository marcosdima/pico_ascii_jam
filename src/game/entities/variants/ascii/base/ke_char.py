from ..ascii import Ascii
from ......types import Color, Pixel


class Ke(Ascii):
	"""Ke ASCII entity (U+309C - ゜katakana).

	Pixelated ゜ using a 3x3 grid.
	"""

	def get_ascii_unicode(self) -> int:
		return 0x309C  # '゜' katakana

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		# Ke (゜) shape - katakana character based on SVG path
		return [
			p(1, 0),
			p(0, 1), p(1, 1), p(2, 1),
			p(1, 2),
		]
