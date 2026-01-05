from ..__composed import Composed
from .....core.parasites import Trigger
from .....core.interfaces import Collider
from ...special.pickaxe import Pickaxe
from ...special.drop import Drop
from ...ascii import Ascii, Entity
from .....types import Anchor, AnchorPosition, Resource, Color


class Rock(Composed, Collider):
    ''' An ASCII entity that represents a rock character. '''
    def receive_damage(self, damage_amount: int = 10):
        self.health -= damage_amount

        if self.health <= 0:
            self.health = 0
            
            # Drop resource.
            drop = self.get_drop_resource()
            drop.set_transform(position=self.transform.position.to_tuple())
            drop.set_color(self.get_color())

            # Hide.
            self.hide()

            # Call scene to follow drop.
            self.scene.follow_instance(drop)

    
    def get_resource(self) -> Resource:
        ''' Get the resource type of the rock. '''
        return Resource.ROCK


    def get_drop_resource(self) -> Drop:
        ''' Get the resource type dropped by the rock. '''
        drop = Drop(scene=self.scene)
        drop.set_resource(self.get_resource())
        drop.set_transform(scale=(6, 6))
        return drop


    ''' Composed abstract methods. '''
    def get_followers(self) -> list[('Entity', AnchorPosition)]:
        # Set hat.
        self.broke = Ascii(scene=self.scene)
        self.broke.set_unicode(0x2022)  # Unicode character '•'
        self.broke.set_transform(scale=(9, 9))

        self.broke_two = Ascii(scene=self.scene)
        self.broke_two.set_unicode(0x005C)  # Unicode character '/'
        self.broke_two.set_transform(scale=(9, 9))

        self.broke_three = Ascii(scene=self.scene)
        self.broke_three.set_unicode(0x0058)  # Unicode character '●'
        self.broke_three.set_transform(scale=(10, 10))
        
        return [
            (self.broke, AnchorPosition.CENTER),
            (self.broke_two, AnchorPosition.CENTER),
            (self.broke_three, AnchorPosition.CENTER),
        ]   


    ''' Entity Overrides. '''
    def get_default_color(self):
        return Color.GRAY


    def get_default_parasites(self):
        return super().get_default_parasites() + [self.collision]


    ''' Entity life cycle overrides. '''
    def setup(self):
        super().setup()

        self.resource = self.get_resource()
        self.max_health = 100 + (self.resource.value * 100)
        self.health = self.max_health
        self.trigger = Trigger(key='e', action=self.receive_damage)

        self.set_transform(scale=(12, 12))


    def update(self, dt):
        super().update(dt)

        color = self.get_color()
        self.broke.set_color(color)
        self.broke_two.set_color(color)
        self.broke_three.set_color(color)
        
        # Calculate right broke.
        per = (self.health / self.max_health) * 100
        if per > 99:
            self.broke.hide()
            self.broke_two.hide()
            self.broke_three.hide()
        elif per > 50:
            self.broke.show()
            self.broke_two.hide()
            self.broke_three.hide()
        elif per > 25:
            self.broke.hide()
            self.broke_two.show()
            self.broke_three.hide()
        else:
            self.broke.hide()
            self.broke_two.hide()
            self.broke_three.show()


    ''' Collider interface implementation. '''
    def on_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            self.add_parasite(self.trigger)


    def on_end_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            self.remove_parasite(self.trigger)


    def on_keep_collision(self, other_collider: 'Collider'):
        if isinstance(other_collider, Pickaxe):
            #print(f'{self.name} is colliding with {other_collider.name}')
            pass


    ''' Ascii overrides. '''
    def get_default_unicode(self) -> int:
        return 0x30ED  # Default character 'ロ'
    

    ''' Followable interface implementation. '''
    def get_follow_anchors(self):
        ''' Set the initial follow positions for the entity. '''
        super().get_follow_anchors()

        # Some basic data.
        x, y = self.transform.position.to_tuple()
        part = self.transform.get_scaled_size() / 10
        

        # Calculate center position.
        x_offset = x + part.x * 4.5
        y_offset = y + part.y * 4.5
        anchor_center = Anchor((x_offset, y_offset))
        
        return {
            AnchorPosition.CENTER: anchor_center
        }   
