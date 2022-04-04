from util import Point
from random import randomint

class Food:
	def __init__(self, width=8, height=8):
	
		list_of_coordinates = [0,1,2,3,4,5,6,7]
		Food_x = sample(list_of_coordinates, 1)
		Food_y = sample(list_of_coordinates, 1)
		coordinates = (Food_x, Food_y)
	
		self.position: coordinates

		#OR
		
		self.position: randint(0,8), randint(0,8)
			

	def get_random_position(self, snake_pos: list[Point]):
		possible_points = [Point(0,0), (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
				  (1,0), (1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7),
				  (2,0), (2,1), (2,2), (2,3), (2,4), (2,5), (2,6), (2,7),
				  (3,0), (3,1), (3,2), (3,3), (3,4), (3,5), (3,6), (3,7),
				  (4,0), (4,1), (4,2), (4,3), (4,4), (4,5), (4,6), (4,7),
				  (5,0), (5,1), (5,2), (5,3), (5,4), (5,5), (5,6), (5,7),
				  (6,0), (6,1), (6,2), (6,3), (6,4), (6,5), (6,6), (6,7),
				  (7,0), (7,1), (7,2), (7,3), (7,4), (7,5), (7,6), (7,7),] - snake_pos
		sample(possible_points, 1)
		pass
