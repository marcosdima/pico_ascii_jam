from ..ascii import Ascii
from ......types import Color, Pixel


class Frame(Ascii):
	"""Frame ASCII entity (30ED)."""
	
	def get_ascii_unicode(self) -> int:
		return 0x30ED

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		return [
			p(0, 0),	p(1, 0),	p(2, 0),	p(3, 0),	p(4, 0),
            p(0, 1),										p(4, 1),
            p(0, 2),										p(4, 2),
            p(0, 3),										p(4, 3),
			p(0, 4),	p(1, 4),	p(2, 4),	p(3, 4),	p(4, 4),
		]
