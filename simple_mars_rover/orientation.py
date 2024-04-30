from abc import ABC


class Orientation(ABC):
    """Cardinal directions."""
    pass


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
