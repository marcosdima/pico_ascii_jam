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
					p(1, 0), p(2, 0),
								 p(3, 1),					 p(5, 1), p(6, 1),
											 p(4, 2),
								 p(3, 3),					 p(5, 3),
															  p(6, 4),
		]
