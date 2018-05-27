import pygame, pytmx, sys
sys.path.insert(0, "Entity")
import Player

class Map:
	def __init__(self, filename):
		tm = pytmx.load_pygame(filename)
		self.width = tm.width * tm.tilewidth
		self.height = tm.height * tm.tileheight
		self.tmxdata = tm

	def render(self, surface):
		ti = self.tmxdata.get_tile_image_by_gid
		for layer in self.tmxdata.visible_layers:
			if isinstance(layer, pytmx.TiledTileLayer):
				for x, y, gid, in layer:
					tile = ti(gid)
					if tile:
						surface.blit(tile, (x * self.tmxdata.tilewidth, y * self.tmxdata.tileheight))

	def make_map(self):
		temp_surface = pygame.Surface((self.width, self.height))
		self.render(temp_surface)
		return temp_surface

class Camera:
	def __init__(self, h):
		self.x = 0
		self.y = 0
		self.zooms = [500, 300, 500]
		print(self.zooms[h])
		self.h = self.zooms[h]
		self.w = int(4/3 * self.h)
