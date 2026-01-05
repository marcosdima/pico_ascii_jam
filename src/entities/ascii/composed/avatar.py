from ..ascii import Entity
from ..special.pickaxe import Pickaxe
from ....types import Anchor, AnchorPosition, Color, ColliderGroup
from ....core.interfaces import Collider
from .__composed import Composed


class Avatar(Composed, Collider):
    ''' An ASCII entity that represents an avatar character. '''


    ''' Composed abstract methods. '''
    def get_followers(self) -> list[('Entity', AnchorPosition)]:
        # Set right
        pickaxe = Pickaxe(scene=self.scene)
        pickaxe.set_transform(scale=(5, 5))

        return [
            (pickaxe, AnchorPosition.CENTER_RIGHT),
        ]   


    ''' Entity Overrides. '''
    def get_default_color(self):
        return Color.YELLOW


    def get_default_parasites(self):
        return super().get_default_parasites() + [self.collision]


    ''' Entity life cycle overrides. '''
    def setup(self):
        super().setup()
        self.set_transform(scale=(10, 10))
        self.transform.z_index = 10


    ''' Ascii overrides. '''
    def get_default_unicode(self) -> int:
        return 0xC6C3  # Default character 'ÆÃ'
    

    ''' Followable interface implementation. '''
    def get_follow_anchors(self):
        ''' Set the initial follow positions for the entity. '''
        super().get_follow_anchors()

        # Some basic data.
        x, y = self.transform.position.to_tuple()
        part = self.transform.get_scaled_size() / 10
        
        # Calculate head position
        x_offset = x + part.x * 4.5
        y_offset = y
        anchor_head = Anchor((x_offset, y_offset))

        # Calculate right hand position.
        x_offset = x + (part.x * 10)
        y_offset = y + part.y * 4
        anchor_right_hand = Anchor((x_offset, y_offset))

        # Calculate center position.
        x_offset = x + part.x * 5
        y_offset = y + part.y * 5
        anchor_center = Anchor((x_offset, y_offset))
        
        return {
            AnchorPosition.TOP_CENTER: anchor_head,
            AnchorPosition.CENTER_RIGHT: anchor_right_hand,
            AnchorPosition.CENTER: anchor_center
        }   


    ''' Collider interface override. '''
    def get_default_collider_group(self) -> 'ColliderGroup':
        return ColliderGroup.PLAYER

