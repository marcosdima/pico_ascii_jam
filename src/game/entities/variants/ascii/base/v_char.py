from ..ascii import Ascii
from ......types import Color, Pixel


class V(Ascii):
	"""V ASCII entity."""
	
	def get_ascii_unicode(self) -> int:
		return 0x0076  # v

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		# V shape
		return [
			p(0, 0),			    p(2, 0),
			p(0, 1),			    p(2, 1),
			p(0, 2),	p(1, 2),	p(2, 2),
						p(1, 3),
		]
