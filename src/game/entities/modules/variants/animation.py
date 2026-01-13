import math
import pymunk
from typing import TYPE_CHECKING, Callable

from .__module import Module
from .....types import Vector2, Color


if TYPE_CHECKING:
    from ...entity import Entity


class AnimationTrack:
    '''Base animation track.'''
    def __init__(self, duration: float):
        self.duration = max(duration, 0.001)
        self.elapsed_time = 0.0
        self.is_finished = False

    
    def update(self, delta_time: float) -> float:
        '''Returns progress (0.0 to 1.0).'''
        if self.is_finished:
            return 1.0
        
        self.elapsed_time += delta_time
        progress = self.elapsed_time / self.duration
        
        if progress >= 1.0:
            self.is_finished = True
            return 1.0
        
        return progress

    
    def reset(self):
        '''Reset animation.'''
        self.elapsed_time = 0.0
        self.is_finished = False


class RotationTrack(AnimationTrack):
    '''Rotation animation.'''
    def __init__(self, duration: float, target_angle: float, clockwise: bool = True):
        super().__init__(duration)
        self.start_angle = 0.0
        self.target_angle = target_angle
        self.clockwise = clockwise

    
    def get_current_angle(self, progress: float) -> float:
        '''Returns current angle based on progress.'''
        angle_diff = self.target_angle - self.start_angle
        
        # Normalizar la diferencia al rango [-π, π]
        while angle_diff > math.pi:
            angle_diff -= 2 * math.pi
        while angle_diff < -math.pi:
            angle_diff += 2 * math.pi
        
        # Si no es en dirección especificada, ajustar
        if not self.clockwise and angle_diff > 0:
            angle_diff -= 2 * math.pi
        elif self.clockwise and angle_diff < 0:
            angle_diff += 2 * math.pi
        
        return self.start_angle + angle_diff * progress


class DisplacementTrack(AnimationTrack):
    '''Displacement animation.'''
    def __init__(self, duration: float, target_position: Vector2):
        super().__init__(duration)
        self.start_position = Vector2(0.0, 0.0)
        self.target_position = target_position

    
    def get_current_position(self, progress: float) -> Vector2:
        '''Returns current position based on progress.'''
        x = self.start_position.x + (self.target_position.x - self.start_position.x) * progress
        y = self.start_position.y + (self.target_position.y - self.start_position.y) * progress
        return Vector2(x, y)


class ColorGradationTrack(AnimationTrack):
    '''Color gradation animation.'''
    def __init__(self, duration: float, target_color: Color):
        super().__init__(duration)
        self.start_color = Color(255, 255, 255, 255)
        self.target_color = target_color

    
    def get_current_color(self, progress: float) -> Color:
        '''Returns current color based on progress.'''
        r = int(self.start_color.r + (self.target_color.r - self.start_color.r) * progress)
        g = int(self.start_color.g + (self.target_color.g - self.start_color.g) * progress)
        b = int(self.start_color.b + (self.target_color.b - self.start_color.b) * progress)
        a = int(self.start_color.a + (self.target_color.a - self.start_color.a) * progress)
        
        return Color(
            max(0, min(255, r)),
            max(0, min(255, g)),
            max(0, min(255, b)),
            max(0, min(255, a))
        )


class Animation(Module):
    '''Animation module: rotation, displacement, color gradation.'''
    
    def setup(self):
        '''Initialize animation tracks.'''
        self.rotation_track: RotationTrack | None = None
        self.displacement_track: DisplacementTrack | None = None
        self.color_track: ColorGradationTrack | None = None
        
        self.on_animation_complete: Callable[[], None] | None = None

    
    def _on_owner_update(self, delta_time: float):
        '''Update active animations.'''
        if self.rotation_track and not self.rotation_track.is_finished:
            progress = self.rotation_track.update(delta_time)
            current_angle = self.rotation_track.get_current_angle(progress)
            self.owner.body.angle = current_angle
            
            if self.rotation_track.is_finished:
                self._check_all_animations_finished()
        
        if self.displacement_track and not self.displacement_track.is_finished:
            progress = self.displacement_track.update(delta_time)
            current_pos = self.displacement_track.get_current_position(progress)
            self.owner.body.position = pymunk.Vec2d(current_pos.x, current_pos.y)
            
            if self.displacement_track.is_finished:
                self._check_all_animations_finished()
        
        if self.color_track and not self.color_track.is_finished:
            progress = self.color_track.update(delta_time)
            current_color = self.color_track.get_current_color(progress)
            self.owner.set_color(current_color)
            
            if self.color_track.is_finished:
                self._check_all_animations_finished()

    
    def _check_all_animations_finished(self):
        '''Check if all animations finished.'''
        all_finished = True
        
        if self.rotation_track and not self.rotation_track.is_finished:
            all_finished = False
        if self.displacement_track and not self.displacement_track.is_finished:
            all_finished = False
        if self.color_track and not self.color_track.is_finished:
            all_finished = False
        
        if all_finished and self.on_animation_complete:
            self.on_animation_complete()

    
    def animate_rotation(self, duration: float, target_angle: float, clockwise: bool = True):
        '''Start rotation animation.'''
        self.rotation_track = RotationTrack(duration, target_angle, clockwise)
        self.rotation_track.start_angle = self.owner.body.angle

    
    def animate_displacement(self, duration: float, target_position: Vector2):
        '''Start displacement animation.'''
        self.displacement_track = DisplacementTrack(duration, target_position)
        current_pos = self.owner.body.position
        self.displacement_track.start_position = Vector2(current_pos.x, current_pos.y)

    
    def animate_color(self, duration: float, target_color: Color):
        '''Start color animation.'''
        self.color_track = ColorGradationTrack(duration, target_color)
        self.color_track.start_color = self.owner.color.copy()

    
    def stop_rotation(self):
        '''Stop rotation.'''
        self.rotation_track = None

    
    def stop_displacement(self):
        '''Stop displacement.'''
        self.displacement_track = None

    
    def stop_color(self):
        '''Stop color animation.'''
        self.color_track = None

    
    def stop_all(self):
        '''Stop all animations.'''
        self.stop_rotation()
        self.stop_displacement()
        self.stop_color()

    
    def is_animating(self) -> bool:
        '''Check if any animation is active.'''
        rotation_active = self.rotation_track and not self.rotation_track.is_finished
        displacement_active = self.displacement_track and not self.displacement_track.is_finished
        color_active = self.color_track and not self.color_track.is_finished
        
        return rotation_active or displacement_active or color_active

    
    def set_on_complete(self, callback: Callable[[], None]):
        '''Set callback when all animations complete.'''
        self.on_animation_complete = callback
