import pymunk


from ...entity import Entity
from .....types import Vector2


class Composed(Entity):
    def __init__(self):
        super().__init__()
        self.__parts: dict[Entity, Vector2] = {}
        self.space_change.add_callback(self.__on_space_change)
        print(f"[Composed] Initialized composed entity id={self.id}")


    def __on_space_change(self, space: pymunk.Space | None):
        ''' Handle parent changed event. '''
        print(self.__parts)
        print(f"[Composed] Space changed for id={self.id} -> {space}")
        for part, offset in self.__parts.items():
            print(f"[Composed] Propagate space to part id={part.id}, offset={offset}")
            part.set_space(space)
            # Follow this composed body's transform
            part.modules.follower.set_target(self.body, offset, angle_offset=part.body.angle, follow_angle=True)

    
    def add_part(self, part: Entity, offset: tuple[float, float]):
        ''' Add a part to the composed entity. '''
        vec = Vector2(*offset)
        self.__parts[part] = vec
        print(f"[Composed] Added part id={part.id} with offset={vec}")

        # Register part lifecycle to this composed entity (like Layout does)
        self.update.add_callback(part.call_update)
        self.draw.add_callback(lambda: part.call_draw(self.base_surface))
        self.handle_event.add_callback(part.handle_event)

        # Ensure it follows this composed body immediately (in case space already set)
        part.modules.follower.set_target(self.body, vec, angle_offset=part.body.angle, follow_angle=True)
    

    def remove_part(self, part: Entity):
        ''' Remove a part from the composed entity. '''
        removed = self.__parts.pop(part, None)
        print(f"[Composed] Removed part id={part.id}, existed={removed is not None}")


