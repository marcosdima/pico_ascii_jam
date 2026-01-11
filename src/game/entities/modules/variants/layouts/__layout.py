from abc import abstractmethod
from typing import TYPE_CHECKING


from ...modules import Module


if TYPE_CHECKING:
    from ....entity import Entity


class Layout(Module):
    ''' Layout module base class. '''
    def setup(self):
        self.components: list["Entity"] = []
        self.settings = {}
        self.components_settings: dict[int, dict] = {}


    def add_component(self, component: 'Entity', settings: dict = {}):
        ''' Add component to be managed by the layout. '''
        self.components.append(component)
        self._set_component_settings(component.id, settings)
        
        self.owner.update.add_callback(component.call_update)
        self.owner.draw.add_callback(lambda: component.call_draw(self.owner.base_surface))
        self.owner.handle_event.add_callback(component.handle_event)


    
    def set_settings(self, settings: dict):
        ''' Set layout settings. '''
        if self._validate_settings(settings):
            self.settings = settings
        else:
            raise ValueError("Invalid layout settings.")
        

    def _set_component_settings(self, component_index: int, settings: dict):
        ''' Set component settings. '''
        if self._validate_component_setting(settings):
            self.components_settings[component_index] = settings
        else:
            raise ValueError("Invalid component settings.")


    def _on_owner_size_changed(self, prev, new):
        self._arrange_components()

    
    def _set_as_follower(self, component: 'Entity', position: tuple[float, float]):
        ''' Move component to position relative to owner. '''
        component.modules.follower.set_target(self.owner.body, offset=position)


    def _get_component_setting_field(self, component_id: int, key: str, default=None):
        ''' Get component setting by index and key. '''
        component_settings = self.components_settings.get(component_id, {})
        return component_settings.get(key, default)


    @abstractmethod
    def _arrange_components(self):
        ''' Handle the layout arrangement. '''
        pass


    @abstractmethod
    def _validate_settings(self, settings: dict) -> bool:
        ''' Validate the layout settings. '''
        pass


    @abstractmethod
    def _validate_component_setting(self, component_setting: dict) -> bool:
        ''' Validate the component settings. '''
        pass


    