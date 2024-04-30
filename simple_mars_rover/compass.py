from simple_mars_rover.orientation import North, South, West, East


class Compass:

    def __init__(self, orientation: str) -> None:
        self.orientation = orientation
        orientations = {
            "N": North,
            "S": South,
            "W": West,
            "E": East
        }
        self._orientation = orientations[self.orientation]()

    def __str__(self) -> str:
        return f"{self.orientation}"

    def __eq__(self, other: str) -> bool:
        return self.orientation == other

    def turn_right(self) -> "Compass":
        orientation = {
            "N": "E",
            "E": "S",
            "S": "W",
            "W": "N"
        }[self.orientation]

        self._orientation = self._orientation.turn_right()

        return Compass(orientation)

    def turn_left(self) -> "Compass":
        orientation = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }[self.orientation]

        self._orientation = self._orientation.turn_left()

        return Compass(orientation)

    def move_y(self, coordinate: int) -> int:
        if self.orientation == "N":
            coordinate += 1
        elif self.orientation == "S":
            coordinate -= 1

        return coordinate

    def move_x(self, coordinate: int) -> int:
        if self.orientation == "E":
            coordinate += 1
        elif self.orientation == "W":
            coordinate -= 1

        return coordinate