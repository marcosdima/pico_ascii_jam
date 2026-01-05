from typing import TYPE_CHECKING


from ..parasite import Parasite
from ....types import AnchorPosition


if TYPE_CHECKING:
    from ...interfaces import Followable


class Follow(Parasite):
    ''' A parasite that makes the target entity follow another entity. '''
    def __init__(
            self,
            followable: 'Followable',
            follow_index: AnchorPosition = AnchorPosition.CENTER
        ):
        super().__init__()
        self.followable = followable
        self.follow_index: AnchorPosition = follow_index
    

    ''' Override methods. '''
    def on_update(self, dt):
        if self.target:
            anchor = self.followable.get_follow_anchor(self).copy()
            scaled_size = self.target.transform.get_scaled_size()
            offset_x, offset_y = 0, 0
            
            if self.follow_index == AnchorPosition.TOP_CENTER:
                offset_x = -scaled_size.x / 2
                offset_y = -scaled_size.y
            elif self.follow_index == AnchorPosition.CENTER_RIGHT:
                offset_x = 0
                offset_y = -scaled_size.y / 2
            elif self.follow_index == AnchorPosition.CENTER:
                offset_x = -scaled_size.x / 2
                offset_y = -scaled_size.y / 2
            
            x = anchor.point.x + offset_x
            y = anchor.point.y + offset_y
            self.target.transform.set_position(x, y)

    
    def on_draw(self):
        pass
    