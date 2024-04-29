

class MarsRover:

    def __init__(self) -> None:
        self.compass = "N"
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
                self.y_coordinate += 1

        return f"0:{self.y_coordinate}:{self.compass}"

    def turn_right(self) -> None:
        self.compass = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }[self.compass]

    def turn_left(self) -> None:
        self.compass = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }[self.compass]
