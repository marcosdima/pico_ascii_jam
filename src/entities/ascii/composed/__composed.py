from ..ascii import Ascii, Entity, abstractmethod
from ....core.interfaces import Followable
from ....core.parasites import Follow
from ....types import Anchor, AnchorPosition


class Composed(Ascii, Followable):
    ''' Combination of ASCII entities that work together. '''


    ''' Entity life cycle overrides. '''
    def setup(self):
        self.set_unicode(self.get_default_unicode())

        super().setup()

        # Set followers.
        for follower, position in self.get_followers():
            self.add_follower(follower, position)


    ''' Abstract methods. '''
    @abstractmethod
    def get_followers(self) -> list[('Entity', AnchorPosition)]:
        pass


    ''' Followable interface implementation. '''
    def add_follower(
            self,
            follower: 'Entity',
            position: AnchorPosition,
        ):
        follow = Follow(self, position)
        follower.add_parasite(follow)
        self.followers.append(follower)