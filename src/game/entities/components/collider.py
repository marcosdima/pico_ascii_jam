from .__base import Base, pygame
from ....types import ColliderGroup, Color
from ....utils import Event


class Collider(Base):
    ''' Collider interface class. '''
    __references: list['Collider'] = []


    def __init__(self):
        super().__init__()

        # Collider group.
        self.group = ColliderGroup.DEFAULT
        self.avoid_groups: set[ColliderGroup] = set()
        self.vip_groups: set[ColliderGroup] = set()

        # Collider areas and colliding references.
        self.__areas: list['Collider'] = []
        self.__colliding: set['Collider'] = set()
        self.__collide: bool = True
        self.__debug_collisions: bool = True
        self.__debug_color: Color = Color.GREEN

        # Register collider reference.
        self.__references.append(self)

        # Add update callback to check for collisions.
        self.update.add_callback(self.__check_collision)

        # Callbacks.
        self.on_collision = Event[Collider]()
        self.on_still_colliding = Event[Collider]()
        self.on_stop_colliding = Event[Collider]()

        # Set defaults.
        self.on_collision.add_callback(lambda other: self.__colliding.add(other))
        self.on_stop_colliding.add_callback(lambda other: self.__colliding.remove(other))


    def __check_collision(self, _) -> bool:
        ''' Check collision with another collider. '''
        if not self.__collide:
            return False
        
        for other in self.__references:
            # No self-collision.d
            if other is self:
                continue
            
            # If there are VIP groups, only check those.
            if self.vip_groups and other.group not in self.vip_groups:
                if other in self.__colliding:
                    self.on_stop_colliding(other)
                continue
            # Avoid groups.
            elif other.group in self.avoid_groups:
                if other in self.__colliding:
                    self.on_stop_colliding(other)
                continue

            # Check collision.
            colliding = False
            for area in self.get_areas():
                # If was already colliding, skip checks.
                if colliding:
                    continue

                # Check area collision.
                for other_area in other.get_areas():
                    if area.colliderect(other_area):
                        colliding = True
                        
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

    
    def disable_collide(self) -> None:
        ''' Disable collision for this collider. '''
        self.__collide = False

    
    def enable_collide(self) -> None:
        ''' Enable collision for this collider. '''
        self.__collide = True


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


    def add_avoid_group(self, group: ColliderGroup) -> None:
        ''' Set collider group. '''
        self.avoid_groups.add(group)


    def add_vip_group(self, group: ColliderGroup) -> None:
        ''' Set collider VIP group. '''
        self.vip_groups.add(group)


    def is_player(self) -> bool:
        ''' Check if this collider belongs to the player group. '''
        return self.group == ColliderGroup.PLAYER