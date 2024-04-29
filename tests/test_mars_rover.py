import pytest

from simple_mars_rover.mars_rover import MarsRover


class TestMarsRover:
    
    def test_rover_is_deployed_at_initial_position(self) -> None:
        rover = MarsRover.deploy()

        position = rover.execute("")

        assert position == "0:0:N"

    @pytest.mark.parametrize(
        "sequence, expected",
        [("R", "0:0:E"), ("RR", "0:0:S"), ("RRR", "0:0:W"), ("RRRR", "0:0:N")]
    )
    def test_rover_can_turn_right(self, sequence: str, expected: str) -> None:
        rover = MarsRover.deploy()

        position = rover.execute(sequence)

        assert position == expected

    @pytest.mark.parametrize(
        "sequence, expected",
        [("L", "0:0:W"), ("LL", "0:0:S"), ("LLL", "0:0:E"), ("LLLL", "0:0:N")]
    )
    def test_rover_can_turn_left(self, sequence: str, expected: str) -> None:
        rover = MarsRover.deploy()

        position = rover.execute(sequence)

        assert position == expected
