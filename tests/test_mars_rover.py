from simple_mars_rover.mars_rover import MarsRover


class TestMarsRover:
    
    def test_rover_is_deployed_at_initial_position(self) -> None:
        rover = MarsRover.deploy()

        position = rover.execute("")

        assert position == "0:0:N"
