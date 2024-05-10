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


class CommandFactory:
    """Generates command objects"""

    @classmethod
    def generate_command(cls, command: str, mars_rover: MarsRover) -> Command:
        command_map = {
            "R": TurnRight,
            "L": TurnLeft,
            "M": Move
        }

        try:
            return command_map[command](mars_rover)
        except KeyError:
            raise ValueError(f"Invalid command: {command}")
