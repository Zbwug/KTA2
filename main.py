import pygame, math, copy
from pygame.locals import *
from Map import *
from Entity import Entity

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")

window = pygame.display.set_mode((1440, 900))
clock = pygame.time.Clock()

windowOpen = True
while windowOpen:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	
	map1 = Map('textures/tmx/level1.tmx')
	map_img = map1.make_map()
	window.blit(map_img, (0, 0))

	Entity.Entity.draw(window)

	pygame.display.flip()
