import sys
sys.path.insert(0, "Entity")
sys.path.insert(0, "Entity/Human")
import Player
import Enemy
import NPC

def initMatrix(self, window, map, keyowned, oldcurrentlevel):
	player = None
	self.mapmatrix = []
	for i in range(map.tmxdata.height):
		self.mapmatrix.append([])
		for j in range(map.tmxdata.width):
			self.mapmatrix[i].append(0)
	for object in map.tmxdata.objects:
		if object.name == 'o':
			self.mapmatrix[int(object.y / 16)][int(object.x / 16)] = 1
		if object.name.startswith('player') and int(object.name[6:]) == oldcurrentlevel:
			player = Player.Player(object.x, object.y, 4, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 2)
			player.entities.remove(player)
			player.entities.insert(0, player)
			if keyowned:
				player.key = True
				player.keyowned = True
				player.inventory.addItem(window, "key")
		if object.name == 'enemy':
			nbAnimsFrames = []
			for i in object.properties['nbAnimsFrames'].split(','):
				nbAnimsFrames.append(int(i))
			pattern = []
			for i in object.properties['pattern'].split(','):
				pattern.append([])
				for j in i.split(';'):
					pattern[len(pattern) - 1].append(int(j))
			Enemy.Enemy(object.x, object.y, int(object.properties['speed']), object.properties['texture'], nbAnimsFrames, 2, player, pattern)
		if object.name == 'npc':
			nbAnimsFrames = []
			for i in object.properties['nbAnimsFrames'].split(','):
				nbAnimsFrames.append(int(i))
			pattern = []
			for i in object.properties['pattern'].split(','):
				pattern.append([])
				for j in i.split(';'):
					pattern[len(pattern) - 1].append(int(j))
			NPC.NPC(object.x, object.y, int(object.properties['speed']), object.properties['texture'], nbAnimsFrames, 2, pattern, object.properties['dialog'])
