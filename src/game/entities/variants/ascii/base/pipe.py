from ..ascii import Ascii
from ......types import Color, Pixel


class Pipe(Ascii):
	"""Pipe ASCII entity (|)."""
	
	def get_ascii_unicode(self) -> int:
		return 0x007C  # |

	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		# Vertical line
		return [
			p(0, 0),
			p(0, 1),
			p(0, 2),
			p(0, 3),
			p(0, 4),
		]
