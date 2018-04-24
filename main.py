import pygame, math, copy, sys
from pygame.locals import *
from Map import *
import Menu
from Entity import Entity
sys.path.insert(0, "Entity")
sys.path.insert(0, "Menu")
import Player
import Button

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")

window = pygame.display.set_mode((1024, 768))

map1 = Map('textures/tmx/level1.tmx')
map_img = map1.make_map()

player = Player.Player(0, 0, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 14)

def f():
	Menu.Menu.menustate = 0
button1 = Button.Button(600, 300, 500, 100, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 54, "Play", f, -1, -1, 1, -1)
def f():
	exit()
button2 = Button.Button(600, 600, 500, 100, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 54, "Quit", f, 0, -1, -1, -1)

menu = Menu.Menu([button1, button2])

clock = pygame.time.Clock()

windowOpen = True
while windowOpen:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	key = pygame.key.get_pressed()

	if key[pygame.K_ESCAPE]:
		Menu.menustate = 1

	if Menu.Menu.menustate == 0:
		window.blit(map_img, (0, 0))
		Entity.draw(window)
		#Entity.collider(window, map1, player)
	else:
		Menu.Menu.menus[Menu.Menu.menustate - 1].draw(window)
	
	pygame.display.flip()

	clock.tick(144)
