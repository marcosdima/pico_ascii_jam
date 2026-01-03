from ..ascii import Ascii, Entity
from ....core.interfaces import Followable
from ....core.parasites import Follow
from ....types import Anchor, AnchorPosition


class Avatar(Ascii, Followable):
    ''' An ASCII entity that represents an avatar character. '''
    def setup(self):
        self.set_unicode(0xC6C3)
        super().setup()


    ''' Followable interface implementation. '''
    def get_follow_anchors(self):
        ''' Set the initial follow positions for the entity. '''
        super().get_follow_anchors()
        
        # Calculate head position
        x, y = self.transform.position.to_tuple()
        part = self.transform.get_scaled_size().x / 10
        x_offset = x + part * 4.5
        y_offset = y

        anchor_head = Anchor((x_offset, y_offset), AnchorPosition.BOTTOM_CENTER)

        return [anchor_head]
    

    ''' Followable interface implementation. '''
    def add_follower(self, follower: 'Entity'):
        follow = Follow(self)
        follower.add_parasite(follow)
        return follow