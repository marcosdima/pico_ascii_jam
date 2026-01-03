from typing import TYPE_CHECKING


from ..parasite import Parasite
from ....types import Anchor, AnchorPosition


if TYPE_CHECKING:
    from ...interfaces import Followable


class Follow(Parasite):
    ''' A parasite that makes the target entity follow another entity. '''
    def __init__(self, followable: 'Followable'):
        super().__init__()
        self.followable = followable
        self.follow_index = 0

    
    def on_update(self, dt):
        if self.target:
            anchor = self.followable.get_follow_anchor(self).copy()

            match anchor.position:
                case AnchorPosition.TOP_LEFT:
                    offset_x = 0
                    offset_y = 0
                case AnchorPosition.TOP_RIGHT:
                    offset_x = self.target.transform.get_scaled_size().x
                    offset_y = 0
                case AnchorPosition.BOTTOM_LEFT:
                    offset_x = 0
                    offset_y = self.target.transform.get_scaled_size().y
                case AnchorPosition.BOTTOM_RIGHT:
                    offset_x = self.target.transform.get_scaled_size().x
                    offset_y = self.target.transform.get_scaled_size().y
                case AnchorPosition.TOP_CENTER:
                    offset_x = self.target.transform.get_scaled_size().x / 2
                    offset_y = 0
                case AnchorPosition.BOTTOM_CENTER:
                    offset_x = self.target.transform.get_scaled_size().x / 2
                    offset_y = self.target.transform.get_scaled_size().y
                case AnchorPosition.CENTER_LEFT:
                    offset_x = 0
                    offset_y = self.target.transform.get_scaled_size().y / 2
                case AnchorPosition.CENTER_RIGHT:
                    offset_x = self.target.transform.get_scaled_size().x    
                    offset_y = self.target.transform.get_scaled_size().y / 2
                case AnchorPosition.CENTER:
                    offset_x = self.target.transform.get_scaled_size().x / 2
                    offset_y = self.target.transform.get_scaled_size().y / 2
            
            self.target.transform.position.x = anchor.point.x - offset_x
            self.target.transform.position.y = anchor.point.y - offset_y

    
    def on_draw(self):
        pass