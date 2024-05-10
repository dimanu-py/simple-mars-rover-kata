from simple_mars_rover.command import TurnRight, TurnLeft
from simple_mars_rover.mars_rover import MarsRover


class MarsRoverController:

    def __init__(self, mars_rover: "MarsRover") -> None:
        self.mars_rover = mars_rover

    def execute(self, command_sequence: str) -> str:
        for command in command_sequence:
            if command == "R":
                to_execute = TurnRight(self.mars_rover)
                to_execute.execute()
            elif command == "L":
                to_execute = TurnLeft(self.mars_rover)
                to_execute.execute()
            else:
                self.mars_rover.process_command(command)
        return str(self.mars_rover)
