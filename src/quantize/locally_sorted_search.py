
class nearest_neighbor():
	def __init__(self, points, bin_size) -> None:
		self.points = points
		self.bin_size = bin_size
		self.cells = {}
		for i in range(0, 255, bin_size):
			for j in range(0, 255, bin_size):
				for k in range(0, 255, bin_size):
					self.cells[(i, j, k)] = points
	
	def query(self, query_point) -> tuple(int, int, int):
		
