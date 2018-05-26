import pygame, sys

class Potentiometer:

	def __init__(self, x, y, w, h, texture, form):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.texture = pygame.image.load(texture)
		self.texture = pygame.transform.scale(self.texture, (int(self.w), int(self.h)))
		self.texturepos = self.texture.get_rect()
		self.form = form

	def draw(self, window):
		if self.form == "Rectangle":
			window.blit(self.texture, self.texturepos, (-self.x, -self.y, 1024, 768))
		if self.form == "Circle":
			pygame.draw.circle(window, pygame.Color(255, 255, 0), (int(self.x), int(self.y) + 8), self.h -5)

	def deplacement(self, window, power):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			self.texturepos = self.texturepos.move(-power, 0)
		if key[pygame.K_RIGHT]:
			self.texturepos = self.texturepos.move(power, 0)
