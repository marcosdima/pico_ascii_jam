import pygame


from .ui import UI
from ...types import Font, Color, Resource, Text
from ...config import FONT_PATH


class Status(UI):
    '''Status UI component that displays game resources.'''
    
    def setup(self):
        '''Setup the status UI.'''
        # Font configuration
        self.font = Font(font_path=FONT_PATH, font_size=16)
        
        # Position and spacing
        self.padding = 10
        self.line_height = 20
        self.icon_spacing = 5
        
        # Unicode icon for resources (filled circle)
        self.resource_icon = chr(0x25CF)  # ●
        
        # Reference to resources (will be set externally)
        self.resources = None


    def set_resources(self, resources):
        '''Set the resources to display.'''
        self.resources = resources


    def draw(self):
        '''Draw the status UI.'''
        if not self.resources:
            return
        
        y_offset = self.padding
        
        # Display each resource
        for resource_type in Resource:
            amount = self.resources.resources.get(resource_type, 0)
            
            # Get color for this resource
            color = resource_type.get_color()
            
            # Render icon
            icon_surface = self.font.render(
                self.resource_icon,
                True,
                color.to_pygame_color()
            )
            
            # Render resource name and amount
            text = Text(f"{resource_type.name.capitalize()}: {amount}")
            text_surface = self.font.render(
                str(text),
                True,
                Color.WHITE.to_pygame_color()
            )
            
            # Draw icon
            self.surface.blit(icon_surface, (self.padding, y_offset))
            
            # Draw text next to icon
            icon_width = icon_surface.get_width()
            self.surface.blit(
                text_surface,
                (self.padding + icon_width + self.icon_spacing, y_offset)
            )
            
            # Move to next line
            y_offset += self.line_height
