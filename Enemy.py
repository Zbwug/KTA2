import sys
sys.path.insert(0, "..")
from Human import Human

class Enemy(Human):
	def __init__(self, x, y, image, nbAnimsFrames, pace, player, pattern):
		super(Enemy, self).__init__(x, y, image, nbAnimsFrames, pace, player, pattern)
		self.pursuit = False

	def setTarget(self):
		if self.pursuit:
			self.target = [self.player.position.x, self.player.position.y]
			if self.hasLost([self.player.position.x, self.player.position.y]):
				self.pursuit = False
				self.patternstate = 0
				self.gotoPattern()
		else:
			self.gotoPattern()
			if self.hasNoticed([self.player.position.x, self.player.position.y]):
				self.pursuit = True

