from ..ascii import Ascii
from ......types import Color, Pixel


class Avatar(Ascii):
	"""Avatar ASCII entity (C6C3)."""
	
	def get_ascii_unicode(self) -> int:
		return 0xC6C3  # Custom

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		return [
			            p(1, 0), p(2, 0), p(3, 0),
			            p(1, 1), p(2, 1), p(3, 1),
			p(0, 2),    p(1, 2), p(2, 2), p(3, 2),      p(4, 2),
			            p(1, 3), p(2, 3), p(3, 3),
			            p(1, 4),		  p(3, 4),
		]
