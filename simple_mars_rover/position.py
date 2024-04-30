class Position:
    """Coordinates of the rover's position"""

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = self._wrap_coordinate(x_coordinate)
        self.y_coordinate = self._wrap_coordinate(y_coordinate)

    @staticmethod
    def _wrap_coordinate(coordinate: int) -> int:
        if coordinate > 9:
            coordinate = 0
        elif coordinate < 0:
            coordinate = 9
        return coordinate

    def __str__(self) -> str:
        return f"{self.x_coordinate}:{self.y_coordinate}"
