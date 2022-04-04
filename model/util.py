from enum import Enum
from collections import namedtuple


# Point = namedtuple("Point", "x y")
class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y


class Direction(Enum):
	UP = Point(0, -1)
	DOWN = Point(0, 1)
	LEFT = Point(-1, 0)
	RIGHT = Point(0, 1)


class Pixel(object):
	def __init__(self, point, color):
		self.point = point
		self.color = color
		
