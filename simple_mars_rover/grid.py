from simple_mars_rover.position import Position


class Grid:

    def __init__(self, width: int, height: int) -> None:
        self.obstacles: list[Position] = []
        self.width = width
        self.height = height

    def is_inside(self, x_coordinate: int, y_coordinate: int) -> bool:
        width_is_inside = 0 <= x_coordinate < self.width
        height_is_inside = 0 <= y_coordinate < self.height
        return width_is_inside and height_is_inside

    def add_obstacle(self, x_coordinate: int, y_coordinate: int) -> None:
        obstacle_position = Position(x_coordinate, y_coordinate)
        self.obstacles.append(obstacle_position)
