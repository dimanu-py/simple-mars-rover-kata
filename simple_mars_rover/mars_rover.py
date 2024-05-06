from enum import StrEnum

from simple_mars_rover.compass import Compass
from simple_mars_rover.orientation import North
from simple_mars_rover.position import Position


class Commands(StrEnum):
    """Possible commands that Rover can execute"""

    MOVE = "M"
    TURN_RIGHT = "R"
    TURN_LEFT = "L"


class MarsRover:

    def __init__(self) -> None:
        self.compass: Compass = Compass(North())
        self.position: Position = Position(0, 0)

    @classmethod
    def deploy(cls) -> "MarsRover":
        """Named constructor"""
        return MarsRover()

    def execute(self, command_sequence: str) -> str:
        for command in command_sequence:
            self._process_command(command)

        return f"{self.position}:{self.compass}"

    def _process_command(self, command: str) -> None:
        if command == Commands.TURN_RIGHT:
            self.turn_right()
        if command == Commands.TURN_LEFT:
            self.turn_left()
        if command == Commands.MOVE:
            self.move_forward()

    def move_forward(self) -> None:
        self.position = self.compass.move(self.position)

    def turn_right(self) -> None:
        self.compass = self.compass.turn_right()

    def turn_left(self) -> None:
        self.compass = self.compass.turn_left()
