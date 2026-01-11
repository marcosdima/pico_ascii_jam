import pymunk


from ...entity import Entity
from .....types import Vector2


class Composed(Entity):
    def __init__(self):
        super().__init__()
        self.__parts: dict[Entity, Vector2] = {}
        self.space_change.add_callback(self.__on_space_change)


    def __on_space_change(self, space: pymunk.Space | None):
        ''' Handle parent changed event. '''
        for part, offset in self.__parts.items():

            part.set_space(space)
            part.modules.follower.set_target(self.body, offset, angle_offset=part.body.angle, follow_angle=True)

    
    def add_part(self, part: Entity, offset: tuple[float, float]):
        ''' Add a part to the composed entity. '''
        vec = Vector2(*offset)
        self.__parts[part] = vec

        # Register part lifecycle to this composed entity (like Layout does)
        self.update.add_callback(part.call_update)
        self.draw.add_callback(lambda: part.call_draw(self.base_surface))
        self.handle_event.add_callback(part.handle_event)

        # Ensure it follows this composed body immediately (in case space already set)
        part.modules.follower.set_target(self.body, vec, angle_offset=part.body.angle, follow_angle=True)
    

    def remove_part(self, part: Entity):
        ''' Remove a part from the composed entity. '''
        self.__parts.pop(part, None)


