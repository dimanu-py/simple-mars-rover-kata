from simple_mars_rover.orientation import North, Orientation
from simple_mars_rover.position import Position


class MarsRover:

    def __init__(self) -> None:
        self.orientation: Orientation = North()
        self.position: Position = Position(0, 0)

    @classmethod
    def deploy(cls) -> "MarsRover":
        """Named constructor"""
        return MarsRover()

    def move_forward(self) -> None:
        self.position = self.orientation.move(self.position)

    def turn_right(self) -> None:
        self.orientation = self.orientation.turn_right()

    def turn_left(self) -> None:
        self.orientation = self.orientation.turn_left()

    def __str__(self) -> str:
        return f"{self.position}:{self.orientation}"