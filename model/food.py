from util import Point
import random

class Food:
	def __init__(self, width=8, height=8):
		self.position: Point

	def get_random_position(self, snake_pos: list[Point]):
		possible_points = [Point(0, 0), ]
		pass



list_of_coordinates = [1,2,3,4,5,6,7,8]

Food_x = sample(list_of_coordinates, 1)
Food_y = sample(list_of_coordinates, 1)

coordinates = (Food_x, Food_y)

food = Food((1,1), coordinates)
