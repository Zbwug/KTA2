import pygame, sys

class Potentiometer:

	def __init__(self, x, y, w, h, color, id):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.rect = pygame.Rect((self.x, self.y, self.w, self.h))
		self.color = color
		self.id = id

	def draw(self, window):
		pygame.draw.rect(window, self.color, self.rect)

	def deplacement(self, window, power):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			self.rect = self.rect.move(-power, 0)
		if key[pygame.K_RIGHT]:
			self.rect = self.rect.move(power, 0)