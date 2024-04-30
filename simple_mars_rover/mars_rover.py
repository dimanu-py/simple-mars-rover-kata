from simple_mars_rover.compass import Compass
from simple_mars_rover.orientation import North
from simple_mars_rover.position import Position


class MarsRover:

    def __init__(self) -> None:
        self.compass: Compass = Compass(North())
        self.position: Position = Position(0, 0)
        self.x_coordinate = 0
        self.y_coordinate = 0

    @classmethod
    def deploy(cls) -> "MarsRover":
        """Named constructor"""
        return MarsRover()

    def execute(self, command_sequence: str) -> str:
        for command in command_sequence:
            if command == "R":
                self.turn_right()
            if command == "L":
                self.turn_left()
            if command == "M":
                self.move_forward()

        return f"{self.position}:{self.compass}"

    def move_forward(self) -> None:
        self.y_coordinate = self.compass.move_y(self.y_coordinate)
        self.x_coordinate = self.compass.move_x(self.x_coordinate)

        self.position = Position(self.x_coordinate, self.y_coordinate)
        self.position = self.compass.move(self.position)

    def turn_right(self) -> None:
        self.compass = self.compass.turn_right()

    def turn_left(self) -> None:
        self.compass = self.compass.turn_left()
