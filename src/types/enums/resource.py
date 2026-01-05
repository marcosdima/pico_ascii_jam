from .__enum import CustomEnum

class Resource(CustomEnum):
    ROCK = 0
    IRON = 1
    GOLD = 2


    @staticmethod
    def from_string(resource_str: str) -> 'Resource':
        '''Convert string to Resource enum.'''
        resource_str = resource_str.lower()
        if resource_str == 'rock':
            return Resource.ROCK
        elif resource_str == 'iron':
            return Resource.IRON
        elif resource_str == 'gold':
            return Resource.GOLD
        else:
            raise ValueError(f'Unknown resource type: {resource_str}')
        

    def __str__(self):
        return self.name.lower()
    