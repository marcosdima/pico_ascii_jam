from .__interface import Interface
from ..types import Event, Transform

class Anfitrion(Interface):
    ''' Anfitrion interface. '''
    def add_event_callback(self, event: Event, callback: callable):
        ''' Add an event callback to the anfitrion. '''
        self.events[event].append(callback)


    def remove_event(self, event: Event):
        ''' Remove all callbacks for an event. '''
        self.events[event] = []


    ''' Anfitrion event methods. '''
    def on_draw(self):
        ''' Anfitrion: Call all draw event callbacks. '''
        for callback in self.events[Event.DRAW]:
            callback()

    
    def on_update(self, delta_time: float):
        ''' Anfitrion: Call all update event callbacks. '''
        for callback in self.events[Event.UPDATE]:
            callback(delta_time)


    def on_transform_changed(self, prev: Transform, new: Transform):
        ''' Anfitrion: Call all transform changed event callbacks. '''
        for callback in self.events[Event.TRANSFORM_CHANGED]:
            callback(prev, new)


    ''' Interface abstract methods. '''
    def set_properties(self):
        self.events = {
            Event.DRAW: [],
            Event.UPDATE: [],
            Event.TRANSFORM_CHANGED: [],
        }
        super().set_properties()