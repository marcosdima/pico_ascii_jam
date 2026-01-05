from ..module import Module, TYPE_CHECKING


if TYPE_CHECKING:
    from ...entity import Entity


class Family(Module):
    ''' Family module. '''
    def add_child(self, child: 'Entity'):
        ''' Add a child entity to the owner. '''
        child.parent = self.owner
        self.owner.children.append(child)


    ''' Module abstract methods. '''
    def setup(self):
        super().setup()
        self.parent: 'Entity' = None
        self.children: set['Entity'] = []
