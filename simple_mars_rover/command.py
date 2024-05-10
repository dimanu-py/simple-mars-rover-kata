from abc import ABC, abstractmethod

from simple_mars_rover.mars_rover import MarsRover


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        """Execute the command"""


class TurnRight(Command):
    """Turn right command"""

    def __init__(self, mars_rover: MarsRover) -> None:
        self.mars_rover = mars_rover

    def execute(self) -> None:
        self.mars_rover.turn_right()


class TurnLeft(Command):
    """Turn left command"""

    def __init__(self, mars_rover: MarsRover) -> None:
        self.mars_rover = mars_rover

    def execute(self) -> None:
        self.mars_rover.turn_left()


class Move(Command):
    """Move command"""

    def __init__(self, mars_rover: MarsRover) -> None:
        self.mars_rover = mars_rover

    def execute(self) -> None:
        self.mars_rover.move_forward()
