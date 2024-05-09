from simple_mars_rover.mars_rover import MarsRover


class MarsRoverController:

    def __init__(self, mars_rover: "MarsRover") -> None:
        self.mars_rover = mars_rover

    def execute(self, command_sequence: str) -> str:
        return self.mars_rover.execute(command_sequence)
