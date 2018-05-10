import pygame, pytmx, sys
from pygame.locals import *
from Map import *
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
	def collider(self, map, player):
		sTile = 16
		collideBloc = pygame.image.load("textures/collision.png")
		key = pygame.key.get_pressed()
		if key[pygame.K_c]:
			for tile_object in map.tmxdata.objects:
				if tile_object.name == 'o':
					posBloc = collideBloc.get_rect().move(int(-camera.x * 1024 / camera.w + 512), int(-camera.y * 1024 / camera.w + 383))
					window.blit(collideBloc, (tile_object.x * 1024 / camera.w + posBloc.x, tile_object.y * 768 / camera.h + posBloc.y))
					posBloc = collideBloc.get_rect().move(int(camera.x * 1024 / camera.w - 512), int(camera.y * 1024 / camera.w - 383))

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
			self.position = self.position.move(int(-camera.x + (position[0] - camera.x) * (1024 / camera.w - 1) + 512), int(-camera.y + (position[1] - camera.y) * (1024 / camera.w - 1) + 383))
			window.blit(self.sprite, self.position, (self.frame * width / self.maxAnimsFrames, self.anim * height / len(self.nbAnimsFrames), width / self.maxAnimsFrames, height / len(self.nbAnimsFrames)))
			self.position = self.position.move(int(camera.x - (position[0] - camera.x) * (1024 / camera.w - 1) - 512), int(camera.y - (position[1] - camera.y) * (1024 / camera.w - 1) - 383))

	def unwalk(self):
		if self.anim >= 4 and self.anim < 8:
			self.anim %= 4
			self.frame = 0

	@staticmethod
	def initAll(self, map):
		for i in range(map.tmxdata.height):
			self.mapmatrix.append([])
			for j in range(map.tmxdata.width):
				self.mapmatrix[i].append(0)
		for object in map.tmxdata.objects:
			if object.name == 'o':
				self.mapmatrix[int(object.y / 16)][int(object.x / 16)] = 1
			"""if object.name == 'player':
				player = Player.Player(object.x, object.y, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 14)"""


