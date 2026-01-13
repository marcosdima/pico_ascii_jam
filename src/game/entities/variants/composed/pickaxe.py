import math
import pymunk
from .__composed import Composed
from ..ascii.base.parentheses import Parentheses
from ..ascii.base.pipe import Pipe
from .....types import Color, Resource, Vector2


class Pickaxe(Composed):
	"""Composed entity representing a pickaxe (pico).

	Built from a parentheses head and a pipe handle.
	"""
	def __init__(self):
		super().__init__()

		self.made_of = Resource.ROCK
		self.damage = self.made_of.value / 2 # Two strikes to break its resource.

		# Build parts
		head = Parentheses(13)
		handle = Pipe(13)

		head.rotate(-90)

		handle.set_color(Color.BROWN)
		head.set_color(Color.GRAY)

		self.add_part(head, offset=(-head.size.x / 8, -head.size.y))
		self.add_part(handle, offset=(handle.size.y * 2.8, (head.size.x / 32) - 1))
		
		# Recharge timer
		self.recharge_time = 1
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
		'''Use pickaxe: stop following, attack, then return with animation.'''
		if self._recharge_timer == 0:
			self._recharge_timer = self.recharge_time
			
			# Stop following player.
			self.modules.follower.stop_following()
			
			# Attack animation.
			self.modules.animation.animate_rotation(
				duration=0.2,
				target_angle=self.body.angle + math.pi * 0.3,
				clockwise=True
			)
			
			current_pos = self.body.position
			self.modules.animation.animate_displacement(
				duration=0.2,
				target_position=Vector2(current_pos.x + 50, current_pos.y - 20)
			)
			
			# When attack completes, return to following position.
			self.modules.animation.set_on_complete(
				lambda: self._return_to_following()
			)
			
			self.trigger = self.modules.instantiator.create_trigger(
				size=(40, 50),
				offset=self.body.position + (70, 0),
			)
			self.trigger.set_entity_shape(self)
			self.trigger.on_resource_enter = self.__on_hit_resource
	
	
	def _return_to_following(self):
		'''Resume following the player.'''
		self.modules.follower.start_following()
	
	
	def _return_to_initial_angle(self, initial_angle: float):
		'''Return to initial angle only (deprecated, kept for compatibility).'''
		self.modules.animation.animate_rotation(
			duration=0.2,
			target_angle=initial_angle,
			clockwise=False
		)
		self.modules.animation.stop_displacement()


	def __on_hit_resource(self, arbiter, space, data):
		'''Callback when pickaxe hits a resource.'''
		print('Pickaxe hit resource!')

		
