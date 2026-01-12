from ....utils import Event


class Life:
    def __init__(self):
        super().__init__()

        # Health values.
        self.current_health = 100.0
        self.max_health = 100.0

        # Events.
        self.on_damage_received = Event[float]()
        self.on_heal = Event[float]()
        self.on_death = Event()


    def heal(self, amount: float):
        ''' Heal by the specified amount. '''
        self.current_health = min(self.current_health + amount, self.max_health)
        self.on_heal(amount)


    def damage(self, amount: float):
        ''' Damage by the specified amount. '''
        self.current_health = max(self.current_health - amount, 0)
        self.on_damage_received(amount)
        if not self.is_alive():
            self.on_death()


    def is_alive(self) -> bool:
        ''' Current health greater than zero. '''
        return self.current_health > 0
    

    def get_health_percentage(self) -> float:
        ''' Get current_health health as a percentage of max health. '''
        return self.current_health / self.max_health
    

    def set_max_health(self, max_health: int):
        ''' Set maximum health and adjust current_health health if necessary. '''
        self.max_health = max_health
        self.current_health = min(self.current_health, self.max_health)


    def set_health(self, health: int):
        '''  Set current_health health directly, clamped between 0 and max health. '''
        self.current_health = max(0, min(health, self.max_health))