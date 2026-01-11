from abc import abstractmethod


from ...modules import Module


class Layout(Module):
    ''' Layout module base class. '''
    def setup(self):
        super().setup()
        self.settings = {}

    
    def set_settings(self, settings: dict):
        ''' Set layout settings. '''
        if self.validate_settings(settings):
            self.settings = settings
        else:
            raise ValueError("Invalid layout settings.")


    def on_owner_update(self, delta_time):
        self.arrange_children()


    @abstractmethod
    def arrange_children(self):
        ''' Handle the layout arrangement. '''
        pass


    @abstractmethod
    def validate_settings(self, settings: dict) -> bool:
        ''' Validate the layout settings. '''
        pass


    