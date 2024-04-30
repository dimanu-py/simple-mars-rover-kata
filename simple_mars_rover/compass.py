class Compass:

    def __init__(self, orientation: str) -> None:
        self.orientation = orientation

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

        return Compass(orientation)

    def turn_left(self) -> "Compass":
        orientation = {
            "N": "W",
            "W": "S",
            "S": "E",
            "E": "N"
        }[self.orientation]

        return Compass(orientation)
