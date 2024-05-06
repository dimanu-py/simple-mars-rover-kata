from abc import ABC, abstractmethod

from simple_mars_rover.position import Position

STEP_SIZE = 1


class Orientation(ABC):
    """Cardinal directions."""

    @abstractmethod
    def turn_right(self) -> "Orientation":
        """Turn right cardinal direction"""

    @abstractmethod
    def turn_left(self) -> "Orientation":
        """Turn left cardinal direction"""

    @abstractmethod
    def move(self, current_position: Position) -> Position:
        """Move the Rover in the correct direction"""


class South(Orientation):
    """South cardinal direction"""
    NAME = "S"

    def turn_right(self) -> Orientation:
        return West()

    def turn_left(self) -> Orientation:
        return East()

    def move(self, current_position: Position) -> Position:
        return Position(current_position.x_coordinate, current_position.y_coordinate - STEP_SIZE)

    def __str__(self) -> str:
        return self.NAME


class East(Orientation):
    """East cardinal direction"""

    NAME = "E"

    def turn_right(self) -> Orientation:
        return South()

    def turn_left(self) -> Orientation:
        return North()

    def move(self, current_position: Position) -> Position:
        return Position(current_position.x_coordinate + STEP_SIZE, current_position.y_coordinate)

    def __str__(self) -> str:
        return self.NAME


class West(Orientation):
    """West cardinal direction"""

    NAME = "W"

    def turn_right(self) -> Orientation:
        return North()

    def turn_left(self) -> Orientation:
        return South()

    def move(self, current_position: Position) -> Position:
        return Position(current_position.x_coordinate - STEP_SIZE, current_position.y_coordinate)

    def __str__(self) -> str:
        return self.NAME


class North(Orientation):
    """North cardinal direction."""

    NAME = "N"

    def turn_right(self) -> Orientation:
        return East()

    def turn_left(self) -> Orientation:
        return West()

    def move(self, current_position: Position) -> Position:
        return Position(current_position.x_coordinate, current_position.y_coordinate + STEP_SIZE)

    def __str__(self) -> str:
        return self.NAME
