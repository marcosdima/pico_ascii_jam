from ..ascii import Ascii
from ......types import Color, Pixel


class CF(Ascii):
	"""CF ASCII entity 25CF."""
	def get_ascii_unicode(self) -> int:
		return 0x25CF  # ● (Black Circle)


	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		return [
			        p(1, 0), p(2, 0), p(3, 0),
			p(0, 1), p(1, 1), p(2, 1),         p(4, 1),
			p(0, 2), p(1, 2), p(2, 2), p(3, 2), p(4, 2),
			p(0, 3), p(1, 3), p(2, 3), p(3, 3), p(4, 3),
			        p(1, 4), p(2, 4), p(3, 4),
		]
