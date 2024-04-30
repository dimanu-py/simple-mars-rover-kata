from simple_mars_rover.orientation import Orientation
from simple_mars_rover.position import Position


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

    def move(self, position: Position) -> Position:
        position = self._orientation.move(position)
        return position
