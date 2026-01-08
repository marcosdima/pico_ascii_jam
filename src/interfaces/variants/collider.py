from ..base import Base, pygame
from ...types import ColliderGroup, Hook, Color


class Collider(Base):
    ''' Collider interface class. '''
    __references: list['Collider'] = []


    def __init__(self):
        super().__init__()

        # Collider group.
        self.group = ColliderGroup.DEFAULT
        self.avoid_groups: set[ColliderGroup] = set()

        # Collider areas and colliding references.
        self.__areas: list['Collider'] = []
        self.__colliding: set['Collider'] = set()
        self.__debug_collisions: bool = True
        self.__debug_color: Color = Color.GREEN

        # Register collider reference.
        self.__references.append(self)

        # Add update callback to check for collisions.
        self.update.add_callback(self.__check_collision)
        self.draw.add_callback(self.__debug_draw_areas)

        # Callbacks.
        self.on_collision = Hook[Collider]()
        self.on_still_colliding = Hook[Collider]()
        self.on_stop_colliding = Hook[Collider]()

        # Set defaults.
        self.on_collision.add_callback(lambda other: self.__colliding.add(other))
        self.on_stop_colliding.add_callback(lambda other: self.__colliding.remove(other))


    def __check_collision(self, _) -> bool:
        ''' Check collision with another collider. '''
        for other in self.__references:
            # No self-collision.
            if other is self:
                continue

            # Check collision.
            for area in self.get_areas():
                # Skip if other collider is in avoid groups.
                if other.group in self.avoid_groups:
                    if other in self.__colliding:
                        self.on_stop_colliding(other)
                    continue
                
                # Check area collision.
                colliding = False
                for other_area in other.get_areas():
                    if area.colliderect(other_area):
                        colliding = True
                        break

                # Handle collision state changes.
                if colliding:
                    already_colliding = other in self.__colliding
                    if not already_colliding:
                        self.on_collision(other)
                    else:
                        self.on_still_colliding(other)
                elif other in self.__colliding:
                    self.on_stop_colliding(other)

        return False

    
    def __debug_draw_areas(self, surface: pygame.Surface):
        ''' Draw collider areas for debugging. '''
        if self.__debug_collisions:
            for area in self.get_areas():
                pygame.draw.rect(
                    surface,
                    self.__debug_color.to_pygame_color(),
                    area,
                    1,
                )


    def get_areas(self) -> list[pygame.Rect]:
        ''' Get collider areas. '''
        return [area.get_rect() for area in self.__areas]


    def add_areas(self, areas: list['Collider']) -> None:
        ''' Add collider areas. '''
        self.__areas.extend(areas)


    def remove_areas(self, areas: list['Collider']) -> None:
        ''' Remove collider areas. '''
        for area in areas:
            if area in self.__areas:
                self.__areas.remove(area)


    def set_group(self, group: ColliderGroup) -> None:
        ''' Set collider group. '''
        self.group = group
