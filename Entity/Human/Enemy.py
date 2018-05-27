from Human import Human
import math

class Enemy(Human):
	def __init__(self, x, y, speed, image, nbAnimsFrames, pace, pattern):
		super(Enemy, self).__init__(x, y, speed, image, nbAnimsFrames, pace, pattern)
		self.pursuit = False
		self.reload = 50

	def setTarget(self, window):
		if self.reload < 50:
			self.reload += 1
		if self.pursuit:
			if self.reload >= 50:
				self.target = [self.entities[0].position.x, self.entities[0].position.y]
			else:
				self.target = [self.position.x, self.position.y]
			if self.hasLost([self.entities[0].position.x, self.entities[0].position.y]):
				self.pursuit = False
				self.patternstate = 0
				self.gotoPattern()
			elif math.sqrt(math.pow(self.entities[0].position.x - self.position.x,2) + math.pow(self.entities[0].position.y - self.position.y,2)) <= 32 and self.reload >= 50:
				self.reload = 0
				self.entities[0].life -= 1
		else:
			self.gotoPattern()
			if self.hasNoticed([self.entities[0].position.x, self.entities[0].position.y]):
				self.pursuit = True
