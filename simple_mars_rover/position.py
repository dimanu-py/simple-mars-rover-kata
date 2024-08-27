from simple_mars_rover.grid import Grid

STEP_SIZE = 1


class Position:
    """Coordinates of the rover's position"""

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = self._wrap_coordinate(x_coordinate)
        self.y_coordinate = self._wrap_coordinate(y_coordinate)

    @staticmethod
    def _wrap_coordinate(coordinate: int) -> int:
        """Wrap around the grid when the rover goes outside the grid.

        This is, when the rover goes outside the grid, it will appear on the opposite side.
        For example, if the rover goes outside the grid at the top, it will appear at the bottom.
        """
        return coordinate % 10

    def north(self) -> "Position":
        return Position(self.x_coordinate, self.y_coordinate + STEP_SIZE)

    def south(self) -> "Position":
        return Position(self.x_coordinate, self.y_coordinate - STEP_SIZE)

    def east(self) -> "Position":
        return Position(self.x_coordinate + STEP_SIZE, self.y_coordinate)

    def west(self) -> "Position":
        return Position(self.x_coordinate - STEP_SIZE, self.y_coordinate)

    def __str__(self) -> str:
        return f"{self.x_coordinate}:{self.y_coordinate}"

    def is_inside(self, grid: Grid) -> bool:
        return grid.is_inside(self.x_coordinate, self.y_coordinate)

    def is_free(self, grid: Grid) -> bool:
        return grid.is_free(self.x_coordinate, self.y_coordinate)
