from simple_mars_rover.grid import Grid
from simple_mars_rover.orientation import North, Orientation
from simple_mars_rover.position import Position


class MarsRover:

    def __init__(self, grid: Grid) -> None:
        self.grid = grid
        self.orientation: Orientation = North()
        self.position: Position = Position(0, 0)

    @classmethod
    def deploy_at_default_grid(cls) -> "MarsRover":
        """Named constructor with default grid."""
        return MarsRover(Grid(10, 10))

    def move_forward(self) -> None:
        new_position = self.orientation.move(self.position)

        if new_position.is_inside(self.grid):
            self.position = new_position

    def turn_right(self) -> None:
        self.orientation = self.orientation.turn_right()

    def turn_left(self) -> None:
        self.orientation = self.orientation.turn_left()

    def __str__(self) -> str:
        return f"{self.position}:{self.orientation}"