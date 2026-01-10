import pygame
from typing import Literal

from .__module import Module
from .....types import Transform


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
                'bounding_box',
                'color',
                'collisions',
            ]
        ] = set(
            (
                # 'update',        # Periodic update logs
                # 'draw',          # Drawing logs
                'transform',     # Transform change logs
                #'events',        # Pygame events logs
                #'keyboard',      # Keyboard input logs
                'mouse',         # Mouse input logs
                'bounding_box',  # Draw bounding box
                'color',
                'collisions',
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

        # Set callbacks for color changes.
        self.owner.on_set_color.add_callback(
            lambda color: self.__debug(f'Color changed to {color}.', category='color')
        )

        # Set callback for collisions.
        self.owner.on_collision.add_callback(
            lambda other: self.__debug(
                f'Collided with entity id={other.id}.',
                category='collisions'
            )
        )
        self.owner.on_still_colliding.add_callback(
            lambda other: self.__debug(
                f'Colliding with id={other.id}.',
                category='collisions'
            )
        )
        self.owner.on_stop_colliding.add_callback(
            lambda other: self.__debug(
                f'Stopped colliding with id={other.id}.',
                category='collisions'
            )
        )


    ''' Module lifecycle methods. '''
    def on_owner_update(self, delta_time: float):
        ''' Called when the owner entity is updated. '''
        if self.timeout <= 0.0:
            self.timeout = self.update_delay

            owner = self.owner
            parent = owner.get_parent() if hasattr(owner, 'get_parent') else None
            children = owner.get_children() if hasattr(owner, 'get_children') else []

            parent_label = (
                f'{type(parent).__name__}#{getattr(parent, "id", "?")}'
                if parent else 'None'
            )
            children_label = (
                ', '.join(
                    f'{type(child).__name__}#{getattr(child, "id", "?")}'
                    for child in children
                )
                if children else 'None'
            )

            local = owner.transform
            global_pos = owner.get_world_position()
            rect = owner.get_rect()
            color = getattr(owner, 'color', None)
            color_label = repr(color) if color is not None else 'None'

            snapshot_lines = [
                f'  delta_time: {delta_time:.4f}s',
                '  hierarchy:',
                f'    parent: {parent_label}',
                f'    children ({len(children)}): {children_label}',
                '  transform:',
                f'    local: pos={local.position}, size={local.size}, scale={local.scale}, z_index={local.z_index}',
                f'    global: pos={global_pos}, rect={rect}',
                '  color:',
                f'    current: {color_label}',
            ]

            self.__debug('\n'.join(snapshot_lines), category='update')
        else:
            self.timeout -= delta_time
            

    def on_owner_draw(self):
        ''' Called when the owner entity is drawn. '''
        self.__debug(
            f'rect={self.owner.get_rect()}, z_index={self.owner.transform.z_index}',
            category='draw'
        )

        # Draw entity bounding box.
        if 'bounding_box' in self.enabled:
            pygame.draw.rect(
                self.owner.base_surface,
                (255, 0, 0),  # Red for bounding box
                self.owner.get_world_rect(),
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
