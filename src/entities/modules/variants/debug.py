import pygame
from typing import Literal

from ..module import Module, Transform


class Debug(Module):
    ''' Debug module class with filtered logging capabilities. '''
    def __debug(self, message: str, category: str):
        ''' Centralized debug message handling. '''
        if category not in self.enabled:
            return
        
        print(f'[{category.upper()}] Entity id={self.owner.id}: {message}')


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        super().setup()

        # Debug configuration.
        self.update_delay = 1.0  # Seconds between update logs.
        self.timeout = 0.0
        
        # Enabled  debug categories.
        self.enabled: set[
            Literal[
                'update',
                'draw',
                'transform',
                'events',
                'keyboard',
                'mouse',
                'bounding_box'
            ]
        ] = set(
            (
                # 'update',        # Periodic update logs
                # 'draw',          # Drawing logs
                'transform',     # Transform change logs
                # 'events',        # Pygame events logs
                'keyboard',      # Keyboard input logs
                'mouse',         # Mouse input logs
                'bounding_box',  # Draw bounding box
            )
        )

        # Set callbacks for input events if input module is present.
        self.owner.mouse_on.add_callback(
            lambda: self.__debug('Mouse entered entity area.', category='mouse')
        )
        self.owner.mouse_exit.add_callback(
            lambda: self.__debug('Mouse exited entity area.', category='mouse')
        )
        self.owner.press_mouse_button.add_callback(
            lambda button: self.__debug(f'Mouse button {button} pressed.', category='mouse')
        )
        self.owner.release_mouse_button.add_callback(
            lambda button: self.__debug(f'Mouse button {button} released.', category='mouse')
        )
        self.owner.press_key.add_callback(
            lambda key: self.__debug(f'Key {key} pressed.', category='keyboard')
        )
        self.owner.release_key.add_callback(
            lambda key: self.__debug(f'Key {key} released.', category='keyboard')
        )


    ''' Module lifecycle methods. '''
    def on_owner_update(self, delta_time: float):
        ''' Called when the owner entity is updated. '''
        if self.timeout <= 0.0:
            self.timeout = self.update_delay
            self.__debug(
                f'delta_time={delta_time:.4f}s, pos={self.owner.get_position()}, size={self.owner.get_size()}',
                category='update'
            )
        else:
            self.timeout -= delta_time
            

    def on_owner_draw(self, surface: pygame.Surface):
        ''' Called when the owner entity is drawn. '''
        self.__debug(
            f'rect={self.owner.get_rect()}, z_index={self.owner.transform.z_index}',
            category='draw'
        )

        # Draw entity bounding box.
        if 'bounding_box' in self.enabled:
            pygame.draw.rect(
                surface,
                (255, 0, 0),  # Red for bounding box
                self.owner.get_rect(),
                2,  # Line thickness
            )


    def on_owner_transform_changed(self, prev: Transform, new: Transform):
        ''' Called when the owner entity transform is changed. '''
        changes = []
        
        if prev.position != new.position:
            changes.append(f'position: {prev.position} -> {new.position}')
        if prev.size != new.size:
            changes.append(f'size: {prev.size} -> {new.size}')
        if prev.scale != new.scale:
            changes.append(f'scale: {prev.scale} -> {new.scale}')
        if prev.z_index != new.z_index:
            changes.append(f'z_index: {prev.z_index} -> {new.z_index}')
        
        if changes:
            self.__debug(', '.join(changes), category='transform')
