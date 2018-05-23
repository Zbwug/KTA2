import pygame, pytmx, sys
from pygame.locals import *
from Map import *
import Map
sys.path.insert(0, "Entity")
import Player

class Entity:
	temp = 0
	entities = []
	mapmatrix = []

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
	def draw(window, camera):
		for i in Entity.entities:
			type(i).render(i, window, camera)
		Entity.temp = (Entity.temp + 1) % 256

	@staticmethod
	def collider(self, map, map_img, player, currentlevel):
		sTile = 16
		collideBloc = pygame.image.load("textures/collision.png")
		key = pygame.key.get_pressed()
		#while Entity.mapmatrix[int(player.position.y / 16)][int(player.position.x / 16)] == 1 or Entity.mapmatrix[int(player.position.y / 16 + 1)][int(player.position.x / 16)] == 1 or Entity.mapmatrix[int(player.position.y / 16)][int(player.position.x / 16 + 1)] == 1 or Entity.mapmatrix[int(player.position.y / 16 + 1)][int(player.position.x / 16 + 1)] == 1:
		#	if player.anim % 4 == 0:
		#		player.position = player.position.move(0, -4)
		#	if player.anim % 4 == 1:
		#		player.position = player.position.move(4, 0)
		#	if player.anim % 4 == 2:
		#		player.position = player.position.move(0, 4)
		#	if player.anim % 4 == 3:
		#		player.position = player.position.move(-4, 0)
		for tile_object in map.tmxdata.objects:
			if tile_object.name == 'exit':
				if tile_object.x <= player.position.x + player.size[0] and tile_object.x + 16 >= player.position.x and tile_object.y <= player.position.y + player.size[1] and tile_object.y + 16 >= player.position.y:
					currentlevel = currentlevel + 1
					map = Map.Map('textures/tmx/level{}.tmx'.format(currentlevel))
					map_img = map.make_map()

	def render(self, window, camera):
		self.sprite = pygame.transform.scale(self.sprite, (int(self.size[0] * 1024 / camera.w), int(self.size[1] * 768 / camera.h)))
		width = self.sprite.get_rect().size[0]
		height = self.sprite.get_rect().size[1]
		position = [self.position.x, self.position.y]
		if self.anim < 4:
			self.position = self.position.move(int(-camera.x + (position[0] - camera.x) * (1024 / camera.w - 1) + 512), int(-camera.y + (position[1] - camera.y) * (1024 / camera.w - 1) + 383))
			window.blit(self.sprite, self.position, (0, self.anim * height / len(self.nbAnimsFrames), width / self.maxAnimsFrames, height / len(self.nbAnimsFrames)))
			self.position = self.position.move(int(camera.x - (position[0] - camera.x) * (1024 / camera.w - 1) - 512), int(camera.y - (position[1] - camera.y) * (1024 / camera.w - 1) - 383))
		if self.anim >= 4 and self.anim < 8:
			if Entity.temp % self.pace == 0:
				self.frame = (self.frame + 1) % self.nbAnimsFrames[self.anim]
			self.position = self.position.move(int(-camera.x + (position[0] - camera.x) * (1024 / camera.w - 1) + 512), int(-camera.y + (position[1] - camera.y) * (1024 / camera.w - 1) + 383))
			window.blit(self.sprite, self.position, (self.frame * width / self.maxAnimsFrames, self.anim * height / len(self.nbAnimsFrames), width / self.maxAnimsFrames, height / len(self.nbAnimsFrames)))
			self.position = self.position.move(int(camera.x - (position[0] - camera.x) * (1024 / camera.w - 1) - 512), int(camera.y - (position[1] - camera.y) * (1024 / camera.w - 1) - 383))
			if self.anim == 4:
				self.position = self.position.move(0, 4)
			elif self.anim == 5:
				self.position = self.position.move(-4, 0)
			elif self.anim == 6:
				self.position = self.position.move(0, -4)
			elif self.anim == 7:
				self.position = self.position.move(4, 0)
		if self.anim >= 8:
			if Entity.temp % self.pace == 0:
				self.frame += 1
			if self.frame == self.nbAnimsFrames[self.anim]:
				self.frame = 0
				self.anim %= 4
			self.position = self.position.move(int(-camera.x + (position[0] - camera.x) * (1024 / camera.w - 1) + 512), int(-camera.y + (position[1] - camera.y) * (1024 / camera.w - 1) + 383))
			window.blit(self.sprite, self.position, (self.frame * width / self.maxAnimsFrames, self.anim * height / len(self.nbAnimsFrames), width / self.maxAnimsFrames, height / len(self.nbAnimsFrames)))
			self.position = self.position.move(int(camera.x - (position[0] - camera.x) * (1024 / camera.w - 1) - 512), int(camera.y - (position[1] - camera.y) * (1024 / camera.w - 1) - 383))

	def unwalk(self):
		if self.anim >= 4 and self.anim < 8:
			self.anim %= 4
			self.frame = 0
