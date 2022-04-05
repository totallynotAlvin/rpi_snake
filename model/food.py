from collections import deque
from util import Point, Color
import random


class Food:
    def __init__(self, width: int, height: int):
        self.color: Color = Color(255, 0, 0)  # Red
        self.position: Point = Point(1, 1)  # TODO: Randomize this

        self.all_points: list(Point) = []
        for x in range(width//100):
        	for y in range(height//100):
        		self.all_points.append(Point(x, y))


    def move_random_position(self, snake_pos: deque[Point]) -> None:
    	# Todo: food cannot appear within the snake body
    	self.position = random.choice(self.all_points)

    def draw(self):
    	pass

		
