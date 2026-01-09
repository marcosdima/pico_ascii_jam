from typing import Literal, TypeAlias, Callable


from .transform.position import Position, Vector2


TrajectoryType: TypeAlias = Literal['linear', 'parabolic', 'circular']
TrajectoryFn = Callable[[float], Position]


LinearFields: TypeAlias = Literal[
    'direction'
]

ParabolicFields: TypeAlias = Literal[
    'gravity'
]


RadiusFields: TypeAlias = Literal[
    'radius'
]


Fields: TypeAlias = dict[LinearFields | ParabolicFields | RadiusFields, Vector2]


class Trajectory:
    ''' Trajectory representation. '''
    def __call__(self, t: float) -> Position:
        self.acc_time += t
        return self.start + self.fn(self.acc_time)
    

    def set(
        self,
        kind: TrajectoryType = 'linear',
        start: Position = Position(0, 0),
        fields: Fields = {},
    ):
        self.kind = kind
        self.start = start
        self.fields = fields
        self.acc_time = 0.0
        self.fn = self.__build()
        

    def __build(self) -> TrajectoryFn:
        if not self.validate_fields(self.fields):
            raise ValueError(f'Fields do not match trajectory type: {self.kind}. \n Fields given: {self.fields}')
        match self.kind:
            case 'linear':
                direction = self.fields.get('direction', Position(1.0, 0.0))
                return lambda t: Position(x=direction.x * t, y=direction.y * t)

            case 'parabolic':
                g = self.fields.get('gravity', 4.9)
                return lambda t: Position(x=t, y=-g * t**2)

            case 'circular':
                r = self.fields.get('radius', 10)
                return lambda t: Position(
                    x=r * t,
                    y=r * (1 - (t - 1) ** 2)
                )

            case _:
                raise ValueError(f'Unknown trajectory: {self.kind}')
            

    def validate_fields(self, fields: Fields) -> bool:
        match self.kind:
            case 'linear':
                return 'direction' in fields
            case 'parabolic':
                return 'gravity' in fields
            case 'circular':
                return 'radius' in fields
            case _:
                return True