import sys
sys.path.insert(0, "Entity")
import Player

def initMatrix(self, map):
	self.mapmatrix = []
	for i in range(map.tmxdata.height):
		self.mapmatrix.append([])
		for j in range(map.tmxdata.width):
			self.mapmatrix[i].append(0)
	for object in map.tmxdata.objects:
		if object.name == 'o':
			self.mapmatrix[int(object.y / 16)][int(object.x / 16)] = 1
		if object.name == 'player':
			Player.Player(object.x, object.y, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 2)
		if object.name == 'enemy':
			Enemy.Enemy(object.x, object.y, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 2, player, [[896, 240], [976, 240], [976, 320], [896, 320]])


