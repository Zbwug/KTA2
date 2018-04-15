import pygame, pytmx
from Map import *

class Obstacle(Map):
	def __init__(self, x, y, w, h):
		self.rect = pygame.Rect(x, y, w, h)
		self.x = x
		self.y = y
		self.rect.x = x
		self.rect.y = y

	def spawn(self):
		for tile_object in map1.tmxdata.objects:
			if tile_object.name == 'wall':
				Obstacle(tile_object.x, tile_object.y, tile_object.width, tile_object.height)
