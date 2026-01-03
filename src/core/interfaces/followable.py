from abc import ABC, abstractmethod


from ...types import Anchor
from ..parasites import Follow


class Followable(ABC):
    ''' Interface for entities that can be followed. '''
    def get_follow_anchor(self, follow: Follow) -> Anchor:
        ''' Get a follow position by index. '''
        index = follow.follow_index
        follow_anchors = self.get_follow_anchors()
        valid_index = index if 0 <= index < len(follow_anchors) else 0
        return follow_anchors[valid_index]
    
    
    ''' Abstract methods. '''
    @abstractmethod
    def get_follow_anchors(self) -> None:
        ''' Set the initial follow positions for the entity. '''
        pass


    @abstractmethod
    def add_follower(self, follower):
        ''' Add a follower. '''
        pass