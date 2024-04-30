from simple_mars_rover.compass import Compass


class MarsRover:

    def __init__(self) -> None:
        self.compass: Compass = Compass("N")
        self.orientation = "N"
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

    def move_forward(self):
        if self.orientation == "N":
            self.y_coordinate += 1
        elif self.orientation == "E":
            self.x_coordinate += 1
        elif self.orientation == "S":
            self.y_coordinate -= 1
        elif self.orientation == "W":
            self.x_coordinate -= 1

    def turn_right(self) -> None:
        self.orientation = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }[self.orientation]

        self.compass = self.compass.turn_right()

    def turn_left(self) -> None:
        self.orientation = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }[self.orientation]

        self.compass = self.compass.turn_left()
