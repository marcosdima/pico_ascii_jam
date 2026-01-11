from ..ascii import Ascii, Pixel
from ......types import Color


class Parentheses(Ascii):
	"""ASCII entity representing parentheses shape."""
	def get_ascii_unicode(self) -> int:
		return ord('(')

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		return [
			p(0, 0),
			    p(1, 1),
			    p(1, 2),
			    p(1, 3),
			p(0, 4),
		]