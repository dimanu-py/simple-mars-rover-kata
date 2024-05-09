import pytest

from simple_mars_rover.mars_rover import MarsRover
from simple_mars_rover.mars_rover_controller import MarsRoverController


class TestMarsRover:

    commands_providers = [
        ("R", "0:0:E"),
        ("RR", "0:0:S"),
        ("RRR", "0:0:W"),
        ("RRRR", "0:0:N"),
        ("L", "0:0:W"),
        ("LL", "0:0:S"),
        ("LLL", "0:0:E"),
        ("LLLL", "0:0:N"),
        ("M", "0:1:N"),
        ("MM", "0:2:N"),
        ("MMMMMMMMM", "0:9:N"),
        ("MMRM", "1:2:E"),
        ("MMMMRRMM", "0:2:S"),
        ("MRMMMLLMM", "1:1:W"),
        ("MMRMMLM", "2:3:N"),
        ("MMMMMMMMMM", "0:0:N"),
        ("RRMM", "0:8:S"),
        ("LM", "9:0:W")
    ]

    def test_rover_is_deployed_at_initial_position(self) -> None:
        rover = MarsRover.deploy()
        controller = MarsRoverController(rover)

        position = controller.execute("")

        assert position == "0:0:N"

    @pytest.mark.parametrize("sequence, expected", commands_providers)
    def test_rover_can_process_commands(self, sequence: str, expected: str) -> None:
        rover = MarsRover.deploy()
        controller = MarsRoverController(rover)

        position = controller.execute(sequence)

        assert position == expected
