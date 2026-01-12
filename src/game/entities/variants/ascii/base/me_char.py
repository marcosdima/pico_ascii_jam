from ..ascii import Ascii
from ......types import Color, Pixel


class Me(Ascii):
	"""Me ASCII entity (U+30E1 - メ katakana).

	Pixelated メ using a 7x5 grid.
	"""
	def get_ascii_unicode(self) -> int:
		return 0x30E1  # 'メ' katakana


	def get_tiles(self) -> list[Pixel]:
		p = self._set_pixel
		# Me (メ) shape - katakana character based on SVG path
		return [
            p(5, 0),
			p(4, 1), p(2, 1),
			p(3, 2),
			p(2, 3), p(4, 3), p(5, 3),
			p(0, 4), p(1, 4),
		]
