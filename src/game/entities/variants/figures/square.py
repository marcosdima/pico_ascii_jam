from ...entity import Entity


class Square(Entity):
    ''' Square entity class. '''
    def __init__(self):
        super().__init__()
        self.modules.set_background()

    
    ''' Entity overrides. '''
    def set_transform(
        self,
        transform = None,
        position = None,
        size: object = None,
        scale = None,
        z_index = None
    ):
        # Accept either a scalar (uniform size) or a (width, height) tuple/list.
        if size is None:
            size_arg = None
        elif isinstance(size, (tuple, list)):
            size_arg = tuple(size)
        else:
            size_arg = (size, size)

        super().set_transform(
            transform=transform,
            position=position,
            size=size_arg,
            scale=scale,
            z_index=z_index,
        )