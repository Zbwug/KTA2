import pygame, pytmx, sys
from pygame.locals import *
from Map import *

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
		self.entities.append(self)

	@staticmethod
	def draw(window):
		for i in Entity.entities:
			i.render(window)
		Entity.temp = (Entity.temp + 1) % 256

	@staticmethod
	def collider(self, map, player):
		sTile = 16
		for tile_object in map.tmxdata.objects:
			top = tile_object.y
			bottom = tile_object.y + sTile
			left = tile_object.x
			right = tile_object.x + sTile
			if tile_object.name == 'obstacle' and player.position.x + sTile >= left and player.position.x <= right and player.position.y + sTile >= top and player.position.y <= bottom:
				player.position.x = prevX
				player.position.y = prevY

	def render(self, window):
		if self.anim < 4:
			window.blit(self.sprite, self.position, (0, self.anim * self.size[1] / len(self.nbAnimsFrames), self.size[0] / self.maxAnimsFrames, self.size[1] / len(self.nbAnimsFrames)))
		if self.anim >= 4 and self.anim < 8:
			if Entity.temp % self.pace == 0:
				self.frame = (self.frame + 1) % self.nbAnimsFrames[self.anim]
			window.blit(self.sprite, self.position, (self.frame * self.size[0] / self.maxAnimsFrames, self.anim * self.size[1] / len(self.nbAnimsFrames), self.size[0] / self.maxAnimsFrames, self.size[1] / len(self.nbAnimsFrames)))
			if self.anim == 4:
				self.position = self.position.move(0, 1)
			elif self.anim == 5:
				self.position = self.position.move(-1, 0)
			elif self.anim == 6:
				self.position = self.position.move(0, -1)
			elif self.anim == 7:
				self.position = self.position.move(1, 0)
		if self.anim >= 8:
			if Entity.temp % self.pace == 0:
				self.frame += 1
			if self.frame == self.nbAnimsFrames[self.anim]:
				self.frame = 0
				self.anim %= 4
			window.blit(self.sprite, self.position, (self.frame * self.size[0] / self.maxAnimsFrames, self.anim * self.size[1] / len(self.nbAnimsFrames), self.size[0] / self.maxAnimsFrames, self.size[1] / len(self.nbAnimsFrames)))

	def unwalk(self):
		if self.anim >= 4 and self.anim < 8:
			self.anim %= 4
			self.frame = 0
