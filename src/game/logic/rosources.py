from ...types import Resource

class Resources:
    ''' Class to manage game resources. '''
    def __init__(self):
        self.resources: dict[Resource, int] = {}


    def recolect(self, resource: Resource, amount: int):
        ''' Recollect a certain amount of a resource. '''
        if resource in self.resources:
            self.resources[resource] += amount
        else:
            self.resources[resource] = amount


    def consume(self, resource: Resource, amount: int) -> bool:
        ''' Consume a certain amount of a resource. Returns True if successful, False otherwise. '''
        if resource in self.resources and self.resources[resource] >= amount:
            self.resources[resource] -= amount
            return True
        return False