from simple_mars_rover.orientation import North, South, West, East, Orientation


class Compass:

    def __init__(self, orientation: Orientation) -> None:
        self._orientation = orientation

    def __str__(self) -> str:
        return f"{self._orientation}"

    def turn_right(self) -> "Compass":
        orientation = self._orientation.turn_right()
        return Compass(orientation)

    def turn_left(self) -> "Compass":
        orientation = self._orientation.turn_left()
        return Compass(orientation)

    def move_y(self, coordinate: int) -> int:
        if isinstance(self._orientation, North):
            coordinate += 1
        elif isinstance(self._orientation, South):
            coordinate -= 1

        return coordinate

    def move_x(self, coordinate: int) -> int:
        if isinstance(self._orientation, East):
            coordinate += 1
        elif isinstance(self._orientation, West):
            coordinate -= 1

        return coordinate
