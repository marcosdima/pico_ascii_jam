import pymunk


from ...entity import Entity
from .....types import Vector2


class Composed(Entity):
    def __init__(self):
        super().__init__()
        self.__parts: dict[Entity, Vector2] = {}
        self.space_change.add_callback(self._on_space_change)


    def _on_space_change(self, space: pymunk.Space | None):
        ''' Handle parent changed event. '''
        for part, offset in self.__parts.items(): 
            part.set_space(space)
            part.modules.follower.set_target(
                body=self.body,
                offset=offset,
                angle_offset=part.body.angle,
                follow_angle=True
            )
        self.create_collision_shapes_from_parts()
        

    def add_part(self, part: Entity, offset: tuple[float, float] = (0, 0)):
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


    def create_collision_shapes_from_parts(self):
        '''Create collision shapes for all parts using the collision component.
        
        Iterates through all parts and creates box shapes at their respective offsets,
        all attached to this composed entity's body. Each shape is rotated according
        to the part's angle.
        '''
        for part, offset in self.__parts.items():
            self.create_box_shape(
                size=part.size.to_tuple(),
                offset=offset.to_tuple(),
                angle=part.body.angle
            )