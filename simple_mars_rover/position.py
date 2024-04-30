class Position:
    """Coordinates of the rover's position"""

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def __str__(self) -> str:
        return f"{self.x_coordinate}:{self.y_coordinate}"
