from simple_mars_rover.command import TurnRight, TurnLeft, Move, CommandFactory
from simple_mars_rover.mars_rover import MarsRover


class MarsRoverController:

    def __init__(self, mars_rover: "MarsRover") -> None:
        self.mars_rover = mars_rover

    def execute(self, command_sequence: str) -> str:
        for command in command_sequence:
            command_to_execute = CommandFactory.generate_command(command, self.mars_rover)
            command_to_execute.execute()

        return str(self.mars_rover)
