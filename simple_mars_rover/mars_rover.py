from simple_mars_rover.compass import Compass


class MarsRover:

    def __init__(self) -> None:
        self.compass: Compass = Compass("N")
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

        return f"{self.x_coordinate}:{self.y_coordinate}:{self.compass}"

    def move_forward(self) -> None:
        self.move_y()
        self.move_x()

    def turn_right(self) -> None:
            self.compass = self.compass.turn_right()

    def turn_left(self) -> None:
            self.compass = self.compass.turn_left()

    def move_y(self) -> None:
        if self.compass == "N":
            self.y_coordinate += 1
        elif self.compass == "S":
            self.y_coordinate -= 1

    def move_x(self):
        if self.compass == "E":
            self.x_coordinate += 1
        elif self.compass == "W":
            self.x_coordinate -= 1
