from util import Direction, Point


class Snake:
    def __init__(self, width, height):
        self.length: int = 1
        self.positions: list[Point] = [Point(width // 2, height // 2)]
        self.direction: Direction = Direction.RIGHT

    def get_head_position(self):
        return self.positions[0]

    def turn(self, new_direction):
        opposite = (new_direction.x * -1, new_direction.y * -1)

        if self.length == 1 or opposite != self.direction:
            self.direction = new_direction
