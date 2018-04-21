import pygame
from pygame.locals import *

class Entity:
	temp = 0
	entities = []

	def __init__(self, x, y, image, nbAnimsFrames, pace):
		self.sprite = pygame.image.load(image)
		self.position = self.sprite.get_rect()
		self.size = self.position.size
		self.position = self.position.move(x, y)
		self.anim = 0
		self.frame = 0
		self.maxAnimsFrames = 0
		for i in nbAnimsFrames:
			if i >= self.maxAnimsFrames:
				self.maxAnimsFrames = i
		self.nbAnimsFrames = nbAnimsFrames
		self.pace = pace
		entities.append(self)

	@classmethod
	def draw(window):
		for i in self.entities:
			i.render(window)
		self.temp = (self.temp + 1) % 256

	def render(window):
		if anim < 4:
			window.blit(sprite, position, (0, anim * size[1] / len(nbAnimsFrames), size[0] / maxAnimsFrames, size[1] / len(nbAnimsFrames)))
		if anim >= 4 and anim < 8:
			if temp % pace == 0:
				frame = (frame + 1) % nbAnimsFrames[i]
			window.blit(sprite, position, (frame * size[0] / maxAnimsFrames, anim * size[1] / len(nbAnimsFrames), size[0] / maxAnimsFrames, size[1] / len(nbAnimsFrames)))
			if anim == 0:
				position = position.move(0, 1)
			if anim == 1:
				position = position.move(-1, 0)
			if anim == 2:
				position = position.move(0, -1)
			if anim == 3:
				position = position.move(1, 0)
		if anim >= 8:
			if Entity.temp % pace == 0:
				frame += 1
			if frame == nbAnimsFrames[anim]:
				frame = 0
				anim %= 4
			window.blit(sprite, position, (frame * size[0] / maxAnimsFrames, anim * size[1] / len(nbAnimsFrames), size[0] / maxAnimsFrames, size[1] / len(nbAnimsFrames)))

	def unwalk():
		if anim >= 4 and anim < 8:
			anim %= 4
			frame = 0
