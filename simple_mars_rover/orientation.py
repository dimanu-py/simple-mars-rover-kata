from abc import ABC, abstractmethod


class Orientation(ABC):
    """Cardinal directions."""

    @abstractmethod
    def turn_right(self) -> "Orientation":
        """Turn right cardinal direction"""

    @abstractmethod
    def turn_left(self) -> "Orientation":
        """Turn left cardinal direction"""


class South(Orientation):
    """South cardinal direction"""

    def turn_right(self) -> Orientation:
        return West()

    def turn_left(self) -> Orientation:
        return East()

    def __str__(self) -> str:
        return "S"


class East(Orientation):
    """East cardinal direction"""

    def turn_right(self) -> Orientation:
        return South()

    def turn_left(self) -> Orientation:
        return North()

    def __str__(self) -> str:
        return "E"


class West(Orientation):
    """West cardinal direction"""

    def turn_right(self) -> Orientation:
        return North()

    def turn_left(self) -> Orientation:
        return South()

    def __str__(self) -> str:
        return "W"


class North(Orientation):
    """North cardinal direction."""

    def turn_right(self) -> Orientation:
        return East()

    def turn_left(self) -> Orientation:
        return West()

    def __str__(self) -> str:
        return "N"
