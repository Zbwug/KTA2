#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame, math, copy, sys
from pygame.locals import *
from Map import *
import Menu
from Entity import Entity
sys.path.insert(0, "Entity")
sys.path.insert(0, "Entity/Human")
sys.path.insert(0, "Menu")
sys.path.insert(0, "HUD")
import Dialog
import Inventory
import Hearts
import Player
import Human
import Enemy
import Button

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")
popsound = pygame.mixer.Sound("textures/hud/pop.wav")
m = False

playerLife = 3


window = pygame.display.set_mode((1024, 768))

def f():
	Menu.Menu.menustate = 0
button1 = Button.Button(380, 300, 250, 70, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 48, "Play", f, -1, -1, 1, -1)
def f():
	exit()
button2 = Button.Button(380, 500, 250, 70, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 48, "Quit", f, 0, -1, -1, -1)

menu = Menu.Menu([button1, button2], "textures/menu/background/")

currentlevel = 1
map1 = Map('textures/tmx/level{}.tmx'.format(currentlevel))
map_img = map1.make_map()

def initMatrix(self, map):
	for i in range(map.tmxdata.height):
		self.mapmatrix.append([])
		for j in range(map.tmxdata.width):
			self.mapmatrix[i].append(0)
	for object in map.tmxdata.objects:
		if object.name == 'o':
			self.mapmatrix[int(object.y / 16)][int(object.x / 16)] = 1
		if object.name == 'player':
			Player.Player(object.x, object.y, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 5)
		if object.name == 'enemy':
			Enemy.Enemy(object.x, object.y, "textures/link.png", [1, 1, 1, 1, 10, 10, 10, 10], 5, player, [[896, 240], [976, 240], [976, 320], [896, 320]])

camera = Camera(0, 0, 500)
initMatrix(Entity, map1)
dCount = 0

script = "scripts/script.txt"
dialog = Dialog.Dialog(40, script, dCount)

inventory = Inventory.Inventory(((1024/2)-int((148*1.5)/2)) + 25, 768- int(39*1.5))

heart1 = Hearts.Hearts(10, 10, "heart")
heart2 = Hearts.Hearts(60, 10, "heart")
heart3 = Hearts.Hearts(110, 10, "heart")

dark1 = Hearts.Hearts(10, 10, "dark")
dark2 = Hearts.Hearts(60, 10, "dark")
dark3 = Hearts.Hearts(110, 10, "dark")


clock = pygame.time.Clock()

windowOpen = True
while windowOpen:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_g:
				m = False

	key = pygame.key.get_pressed()

	if key[pygame.K_ESCAPE]:
		Menu.Menu.menustate = 1

	if Menu.Menu.menustate == 0:
		camera.x = Entity.entities[0].position.x
		camera.y = Entity.entities[0].position.y
		if camera.x - camera.w/2 < 0:
			camera.x = camera.w/2		
		if camera.y - camera.h/2 < 0:			
			camera.y = camera.h/2		
		if camera.x + camera.w/2 > map1.width:			
			camera.x = map1.width - camera.w/2		
		if camera.y + camera.h/2 > map1.height:
			camera.y = map1.height - camera.h/2

		map_img = pygame.transform.scale(map_img, (int(1600 * 1024 / camera.w), int(1600 * 1024 / camera.w)))
		
		
		
		posmap = map_img.get_rect()

		posmap = posmap.move(int(-camera.x * 1024 / camera.w + 512), int(-camera.y * 1024 / camera.w + 383))
		window.blit(map_img, posmap)
		posmap = posmap.move(int(camera.x * 1024 / camera.w - 512), int(camera.y * 1024 / camera.w - 383))

		Entity.draw(window, camera)
		Entity.collider(window, map1, map_img, Entity.entities[0], currentlevel)
		inventory.box(window)
		if playerLife == 3:
			heart1.box(window)
			heart2.box(window)
			heart3.box(window)
		elif playerLife == 2:
			heart1.box(window)
			heart2.box(window)
			dark3.box(window)
		elif playerLife == 1:
			heart1.box(window)
			dark2.box(window)
			dark3.box(window)
		else:
			dark1.box(window)
			dark2.box(window)
			dark3.box(window)
			Menu.Menu.menustate = 1
			playerLife = 3
		
	else:
		Menu.Menu.menus[Menu.Menu.menustate - 1].draw(window)
	if key[pygame.K_g]:
		if not m:
			popsound.play()
			dCount += 1
			playerLife -= 1
			m = True
		if dCount <= dialog.maxLines():
			Dialog.Dialog(40, script, dCount).box(window)
	pygame.display.flip()

	clock.tick(144)
