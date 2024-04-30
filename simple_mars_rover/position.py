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

    def __str__(self) -> str:
        return f"{self.x_coordinate}:{self.y_coordinate}"
