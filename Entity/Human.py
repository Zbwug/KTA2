import sys
sys.path.insert(0, "..")
from Entity import Entity
import math

class Human(Entity):
	def __init__(self, x, y, image, nbAnimsFrames, pace, target):
		super(Human, self).__init__(x, y, image, nbAnimsFrames, pace)
		self.target = target

	def render(self, window):
		super(Human, self).render(window)
		if self.position.x % 16 == 0 and self.position.y % 16 == 0:
			path = self.astar()
			if len(path) >= 2:
				if path[1][1] - path[0][1] == 1:
					self.anim = 4
				if path[1][0] - path[0][0] == -1:
					self.anim = 5
				if path[1][1] - path[0][1] == -1:
					self.anim = 6
				if path[1][0] - path[0][0] == 1:
					self.anim = 7
			else:
				self.unwalk()

	def astar(self):
		mapmatrix = Entity.mapmatrix
		start = [int(self.position.x / 16), int(self.position.y / 16)]
		finish = [int(self.target.position.x / 16), int(self.target.position.y / 16)]
		if start == finish:
			return []
		openlist = []
		closedlist = [start]
		min = [start[0], start[1], 1000000000, 0, 0]
		while min[0] != finish[0] or min[1] != finish[1]:
			closedlist.append(min)
			if min in openlist:
				openlist.remove(min)
			for i in range(-1, 2):
				for j in range(-1, 2):
					if min[0] + i >= 0 and min[0] + i < len(mapmatrix) and min[1] + j >= 0 and min[1] + j < len(mapmatrix[0]) and mapmatrix[min[1] + j][min[0] + i] == 0 and abs(i) + abs(j) != 2 and abs(i) + abs(j) != 0:
						found = False
						for c in closedlist:
							if c[0] == min[0] + i and c[1] == min[1] + j:
								found = True
						if not found:
							openlist.append([min[0] + i, min[1] + j, math.sqrt(math.pow(min[0] + i - finish[0], 2) + math.pow(min[1] + j - finish[1], 2)), min[0], min[1]])
			min = openlist[0]
			for o in openlist:
				if o[2] < min[2]:
					min = o
		path = []
		path.append(min)
		mapmatrix[min[0]][min[1]] = 2
		while path[len(path) - 1] != start:
			for c in closedlist:
				if c[0] == min[3] and c[1] == min[4]:
					min = c
					path.append(min)
					break
		result = []
		for i in range(len(path)):
			result.append(path[len(path) - 1 - i])
		return result
