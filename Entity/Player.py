import pygame, sys, math
sys.path.insert(0, "HUD")
sys.path.insert(0, "Entity/Human")
from pygame.locals import *
from Entity import Entity
from Inventory import *
from Enemy import Enemy
from NPC import NPC

class Player(Entity):
	def __init__(self, x, y, speed, image, nbAnimsFrames, pace):
		super(Player, self).__init__(x, y, speed, image, nbAnimsFrames, pace)
		self.inventory = Inventory(((1024/2)-int((148*1.5)/2)) + 25, 768- int(39*1.5), self)
		self.spacepressed = False
		self.moving = True
		self.life = 3

	def render(self, window, camera):
		super(Player, self).render(window, camera)
		key = pygame.key.get_pressed()
		if self.moving:
			if key[pygame.K_DOWN] and Entity.mapmatrix[int((self.position.y + 4) / 16 + 1)][int((self.position.x + 0) / 16)] != 1 and Entity.mapmatrix[int((self.position.y + 4) / 16 + 1)][int((self.position.x + 0) / 16 + 1)] != 1:
				self.anim = 4
			elif key[pygame.K_LEFT] and Entity.mapmatrix[int((self.position.y + 0) / 16)][int((self.position.x - 4) / 16)] != 1 and Entity.mapmatrix[int((self.position.y + 0) / 16 + 1)][int((self.position.x - 4) / 16)] != 1:
				self.anim = 5
			elif key[pygame.K_UP] and Entity.mapmatrix[int((self.position.y - 4) / 16)][int((self.position.x + 0) / 16)] != 1 and Entity.mapmatrix[int((self.position.y - 4) / 16)][int((self.position.x + 0) / 16 + 1)] != 1:
				self.anim = 6
			elif key[pygame.K_RIGHT] and Entity.mapmatrix[int((self.position.y + 0) / 16)][int((self.position.x + 4) / 16 + 1)] != 1 and Entity.mapmatrix[int((self.position.y + 0) / 16 + 1)][int((self.position.x + 4) / 16 + 1)] != 1:
				self.anim = 7
			else:
				self.unwalk()

		if key[pygame.K_SPACE]:
			if not self.spacepressed and self.moving:
				if self.anim % 4 == 0:
					self.interact(int(self.position.x / 16), int(self.position.y / 16 + 1))
				if self.anim % 4 == 1:
					self.interact(int(self.position.x / 16 - 1), int(self.position.y / 16))
				if self.anim % 4 == 2:
					self.interact(int(self.position.x / 16), int(self.position.y / 16 - 1))
				if self.anim % 4 == 3:
					self.interact(int(self.position.x / 16 + 1), int(self.position.y / 16))
				self.spacepressed = True
		else:
			self.spacepressed = False

	def interact(self, x, y):
		for e in Entity.entities:
			if e != self:
				if math.sqrt(math.pow(int(e.position.x / 16) - x, 2) + math.pow(int(e.position.y / 16) - y, 2)) <= 3:
					if type(e) is NPC:
						self.moving = False
						e.dialog = 0
					if type(e) is Enemy:
						Entity.entities.remove(e)
					break
