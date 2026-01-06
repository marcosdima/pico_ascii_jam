import pygame
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


    def get_event_callbacks(self, event: Event) -> list[callable]:
        ''' Get all callbacks for an event. '''
        return self.events.get(event, [])


    ''' Interface event methods. '''
    def on_draw(self):
        for callback in self.get_event_callbacks(Event.DRAW):
            callback()

    
    def on_update(self, delta_time: float):
        for callback in self.get_event_callbacks(Event.UPDATE):
            callback(delta_time)


    def on_transform_changed(self, prev: Transform, new: Transform):
        for callback in self.get_event_callbacks(Event.TRANSFORM_CHANGED):
            callback(prev, new)

        
    def on_event(self, event: pygame.event.Event):
        for callback in self.get_event_callbacks(Event.PYGAME_EVENT):
            callback(event)


    ''' Interface abstract methods. '''
    def set_properties(self):
        self.events = {
            Event.DRAW: [],
            Event.UPDATE: [],
            Event.TRANSFORM_CHANGED: [],
            Event.PYGAME_EVENT: [],
        }
        super().set_properties()