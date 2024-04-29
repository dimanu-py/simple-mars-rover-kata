import pytest

from simple_mars_rover.mars_rover import MarsRover


class TestMarsRover:
    
    def test_rover_is_deployed_at_initial_position(self) -> None:
        rover = MarsRover.deploy()

        position = rover.execute("")

        assert position == "0:0:N"

    def test_rover_can_turn_right_with_single_commands(self) -> None:
        rover = MarsRover.deploy()

        assert rover.execute("R") == "0:0:E"
        assert rover.execute("R") == "0:0:S"
        assert rover.execute("R") == "0:0:W"
        assert rover.execute("R") == "0:0:N"

    @pytest.mark.parametrize(
        "sequence, expected",
        [("RR", "0:0:S"), ("RRR", "0:0:W"), ("RRRR", "0:0:N")]
    )
    def test_rover_can_turn_right_with_multiple_commands_in_the_same_sequence(self, sequence: str, expected: str) -> None:
        rover = MarsRover.deploy()

        assert rover.execute(sequence) == expected
