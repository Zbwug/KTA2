import pygame, math, copy, sys
from pygame.locals import *
from Map import *
import Menu
from Entity import Entity
sys.path.insert(0, "Entity")
sys.path.insert(0, "Menu")
import Player
import Human
import Button

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")

window = pygame.display.set_mode((1024, 768))

def f():
	Menu.Menu.menustate = 0
button1 = Button.Button(380, 300, 250, 70, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 48, "Play", f, -1, -1, 1, -1)
def f():
	exit()
button2 = Button.Button(380, 500, 250, 70, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 48, "Quit", f, 0, -1, -1, -1)

menu = Menu.Menu([button1, button2], "textures/menu/background/")

map1 = Map('textures/tmx/level1.tmx')
map_img = map1.make_map()

Entity.initAll(map1)
player = Player.Player(1680, 500, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 14)
camera = Camera(0, 0, 768/2)
npc = Human.Human(160, 0, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 14, player, [[10, 0], [30, 0], [30, 20], [10, 20]])

clock = pygame.time.Clock()

windowOpen = True
while windowOpen:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()

	key = pygame.key.get_pressed()

	if key[pygame.K_ESCAPE]:
		Menu.Menu.menustate = 1

	if Menu.Menu.menustate == 0:
		camera.x = player.position.x
		camera.y = player.position.y
		map_img = pygame.transform.scale(map_img, (int(1600 * 1024 / camera.w), int(1600 * 1024 / camera.w)))
		posmap = map_img.get_rect()
		
		posmap = posmap.move(int(-camera.x / 1024 + 512), int(-camera.y / 1024 + 383))
		window.blit(map_img, posmap)
		posmap = posmap.move(int(camera.x / 1024 - 512), int(camera.y / 1024 - 383))

		Entity.draw(window, camera)
		#Entity.collider(window, map1, player)
	else:
		Menu.Menu.menus[Menu.Menu.menustate - 1].draw(window)

	pygame.display.flip()

	clock.tick(144)
