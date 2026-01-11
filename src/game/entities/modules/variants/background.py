from .__module import Module


class Background(Module):
    ''' Background module class. '''


    ''' Abstract methods. '''
    def setup(self):
        ''' Setup the module. '''
        super().setup()
        self.update_delay = 10.0 # Seconds.
        self.timeout = 0.0


    ''' Module lifecycle methods. '''
    def on_owner_draw(self):
        ''' Called when the owner entity is drawn. '''
        for shape in self.owner.body.shapes:
            self.owner.draw_rect(shape, self.owner.color)
