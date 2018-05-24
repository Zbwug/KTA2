import pygame

class Button:
	def __init__(self, x, y, w, h, texture, font, sFont, text, func, z, q, s, d):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.sprite = pygame.image.load(texture)
		self.sprite = pygame.transform.scale(self.sprite, (w, 3 * h))
		self.position = self.sprite.get_rect()
		self.position = self.position.move(x, y)
		self.size = self.position.size
		self.font = pygame.font.Font(font, sFont)
		self.text = text
		self.func = func
		self.z = z
		self.q = q
		self.s = s
		self.d = d
