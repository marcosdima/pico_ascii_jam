from ..interfaces import Anfitrion, Coloreable, Visible


class Join(Anfitrion, Coloreable, Visible):
    __count = 0

    ''' Python specific methods. '''
    def __init__(self):
        super().__init__()

        # Set id.
        self.id = Join.__count
        Join.__count += 1

    
    def __str__(self):
        return f'<Join id={id(self)}>'