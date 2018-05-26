import pygame
import math
import sys
sys.path.insert(0, "HUD")
from Human import Human
import Dialog

class NPC(Human):
	def __init__(self, x, y, speed, tex, nbAnimsFrames, pace, pattern, dialogfile):
		super(NPC, self).__init__(x, y, speed, tex, nbAnimsFrames, pace, pattern)
		self.dialog = -1
		self.spacepressed = False
		self.dialogfile = dialogfile

	def setTarget(self, window):
		if self.dialog == -1:
			self.gotoPattern()
		else:
			key = pygame.key.get_pressed()
			dialogobj = Dialog.Dialog(100, self.dialogfile, self.dialog)
			if key[pygame.K_SPACE]:
				if not self.spacepressed:
					self.dialog = (self.dialog + 2) % dialogobj.maxLines() - 1
					if self.dialog == -1:
						self.entities[0].moving = True
					self.spacepressed = True
			else:
				self.spacepressed = False
			dialogobj.box(window)
			target = [self.position.x, self.position.y]
			angle = 0
			if self.entities[0].position.x != self.position.x:
				angle = -math.atan((self.entities[0].position.y - self.position.y)/(self.entities[0].position.x - self.position.x))
			else:
				if self.position.y >= self.entities[0].position.y:
					angle = -math.pi/2
				else:
					angle = math.pi/2

			if self.position.x <= self.entities[0].position.x:
				if angle >= math.pi/4:
					self.anim = 2
				elif angle <= -math.pi/4:
					self.anim = 0
				else:
					self.anim = 3
			else:
				if angle >= math.pi/4:
					self.anim = 0
				elif angle <= -math.pi/4:
					self.anim = 2
				else:
					self.anim = 1
