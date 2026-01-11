from .__module import Module


class Background(Module):
    ''' Background module class. '''
    def setup(self):
        self.update_delay = 10.0 # Seconds.
        self.timeout = 0.0

    def _on_owner_draw(self):
        ''' Called when the owner entity is drawn. '''
        print(f"[Background] Draw owner id={self.owner.id} size={self.owner.size} color={self.owner.color}")
        self.owner.draw_rect(size=self.owner.size.to_tuple(), color=self.owner.color)
