from .__composed import Composed
from ..ascii.base.parentheses import Parentheses
from ..ascii.base.pipe import Pipe
from .....types import Color, Resource, ColliderGroup


class Pickaxe(Composed):
	"""Composed entity representing a pickaxe (pico).

	Built from a parentheses head and a pipe handle.
	"""
	def __init__(self):
		super().__init__()

		self.made_of = Resource.ROCK
		self.damage = self.made_of.value / 10

		# Parts.
		head = Parentheses()
		handle = Pipe()

		s = 1
		head.set_size((20 * s, 50 * s))
		handle.set_size((10 * s, 50 * s))

		head.rotate(-90)

		handle.set_color(Color.BROWN)
		head.set_color(Color.GRAY)

		self.add_part(handle, offset=(0, handle.size.y / 4))
		self.add_part(head, offset=(0, -head.size.y / 4))

		# Recharge timer.
		self.recharge_time = 2  # seconds between uses
		self._recharge_timer = 0.0
		self.update.add_callback(self._update_recharge)


	def _update_recharge(self, dt: float):
		'''Update recharge timer.'''
		if self._recharge_timer > 0:
			self._recharge_timer -= dt
			if self._recharge_timer < 0:
				self._recharge_timer = 0


	def charged(self) -> bool:
		'''Check if the pickaxe is charged and ready to use.'''
		return self._recharge_timer == 0


	def use(self):
		'''Simulate using the pickaxe.'''
		if self._recharge_timer == 0:
			self._recharge_timer = self.recharge_time
			trigger = self.modules.instantiator.create_trigger(
				size=(100, 100),
				offset=self.body.position + (50, 0),
			)
			trigger.on_resource_enter = self.__on_hit_resource


	def __on_hit_resource(self, arbiter, space, data):
		'''Callback when pickaxe hits a resource.'''
		shape_a, shape_b = arbiter.shapes
		other = shape_a if shape_b.entity == self else shape_b
		print(other.entity.__class__)
		return True
			

		
