from abc import ABC, abstractmethod


class Orientation(ABC):
    """Cardinal directions."""

    @abstractmethod
    def turn_right(self) -> "Orientation":
        """Turn right cardinal direction"""

    @abstractmethod
    def turn_left(self) -> "Orientation":
        """Turn left cardinal direction"""


class East(Orientation):
    pass


class West(Orientation):
    pass


class North(Orientation):
    """North cardinal direction."""

    def turn_right(self) -> Orientation:
        return East()

    def turn_left(self) -> Orientation:
        return West()
