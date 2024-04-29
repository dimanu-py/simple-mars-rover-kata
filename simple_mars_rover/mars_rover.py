

class MarsRover:

    def __init__(self) -> None:
        self.compass = "N"

    @classmethod
    def deploy(cls) -> "MarsRover":
        """Named constructor"""
        return MarsRover()

    def execute(self, command_sequence: str) -> str:
        for command in command_sequence:
            if command == "R":
                self.turn_right()
        return f"0:0:{self.compass}"

    def turn_right(self) -> None:
        self.compass = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }[self.compass]
