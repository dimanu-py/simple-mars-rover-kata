class Position:
    """Coordinates of the rover's position"""

    def __init__(self, x_coordinate: int, y_coordinate: int) -> None:
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

        if self.x_coordinate > 9:
            self.x_coordinate = 0
        elif self.x_coordinate < 0:
            self.x_coordinate = 9

        if self.y_coordinate > 9:
            self.y_coordinate = 0
        elif self.y_coordinate < 0:
            self.y_coordinate = 9

    def __str__(self) -> str:
        return f"{self.x_coordinate}:{self.y_coordinate}"
