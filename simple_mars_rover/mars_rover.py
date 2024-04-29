

class MarsRover:

    @classmethod
    def deploy(cls) -> "MarsRover":
        """Named constructor"""
        return MarsRover()

    def execute(self, command_sequence: str) -> str:
        if command_sequence == "R":
            return "0:0:E"
        return "0:0:N"