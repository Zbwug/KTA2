import pygame, math, copy, sys
from pygame.locals import *
from Map import *
from Entity import Entity
sys.path.insert(0, "Entity")
import Player
 
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")

window = pygame.display.set_mode((1440, 900))

map1 = Map('textures/tmx/level1.tmx')
map_img = map1.make_map()

player = Player.Player(0, 0, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 14)

clock = pygame.time.Clock()

windowOpen = True
while windowOpen:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	window.blit(map_img, (0, 0))
	Entity.draw(window)
	#Entity.collider(window, map1, player)
	pygame.display.flip()

	clock.tick(144)
