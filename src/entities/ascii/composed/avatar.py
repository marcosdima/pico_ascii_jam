from ..ascii import Ascii, Entity
from ..special.pickaxe import Pickaxe
from ....types import Anchor, AnchorPosition
from .__composed import Composed


class Avatar(Composed):
    ''' An ASCII entity that represents an avatar character. '''


    ''' Composed abstract methods. '''
    def get_followers(self) -> list[('Entity', AnchorPosition)]:
        # Set hat.
        hat = Ascii(surface=self.surface)
        hat.set_unicode(0x30E6)  # Unicode character 'ユ'
        hat.set_transform(scale=(7, 7))

        # Set right
        pickaxe = Pickaxe(surface=self.surface)
        pickaxe.set_transform(scale=(5, 5))

        return [
            (hat, AnchorPosition.TOP_CENTER),
            (pickaxe, AnchorPosition.CENTER_RIGHT),
        ]   


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
