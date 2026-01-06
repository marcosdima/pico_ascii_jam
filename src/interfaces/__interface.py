from abc import ABC, abstractmethod


from ..types import Transform


class Interface(ABC):
    def __init__(self):
        self.set_properties()
        super().__init__()
        

    @abstractmethod
    def set_properties(self) -> None:
        """Setup method to initialize the interface."""
        pass
