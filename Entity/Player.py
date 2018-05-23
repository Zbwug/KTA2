import pygame, sys
from pygame.locals import *
from Entity import Entity

class Player(Entity):
	def __init__(self, x, y, image, nbAnimsFrames, pace):
		super(Player, self).__init__(x, y, image, nbAnimsFrames, pace)

	def render(self, window, camera):
		super(Player, self).render(window, camera)
		key = pygame.key.get_pressed()
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
