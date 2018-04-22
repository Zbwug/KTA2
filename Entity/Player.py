import pygame, sys
from pygame.locals import *
from Entity import Entity

class Player(Entity):
	def __init__(self, x, y, image, nbAnimsFrames, pace):
		super(Player, self).__init__(x, y, image, nbAnimsFrames, pace)

	def render(self, window):
		super(Player, self).render(window)
		key = pygame.key.get_pressed()
		
		prevX = self.position.x
		prevY = self.position.y

		if key[pygame.K_DOWN]:
			self.anim = 4
		elif key[pygame.K_LEFT]:
			self.anim = 5
		elif key[pygame.K_UP]:
			self.anim = 6
		elif key[pygame.K_RIGHT]:
			self.anim = 7
		else:
			self.unwalk()
