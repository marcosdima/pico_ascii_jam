from abc import ABC, abstractmethod


from ...types import Anchor, AnchorPosition
from ..parasites import Follow


class Followable(ABC):
    ''' Interface for entities that can be followed. '''
    def get_follow_anchor(self, follow: Follow) -> Anchor:
        ''' Get a follow position by index. '''
        index = follow.follow_index
        follow_anchors = self.get_follow_anchors()
        return follow_anchors[index]
    

    ''' Python special methods. '''
    def __init__(self):
        super().__init__()
        self.followers = []

    
    ''' Abstract methods. '''
    @abstractmethod
    def get_follow_anchors(self) -> dict[AnchorPosition, Anchor]:
        ''' Set the initial follow positions for the entity. '''
        pass


    @abstractmethod
    def add_follower(self, follower, position: AnchorPosition = AnchorPosition.CENTER):
        ''' Add a follower. '''
        pass