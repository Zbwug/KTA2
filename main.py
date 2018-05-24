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
import Button
import Dialog
import Enemy
import Hearts
import Human
import Inventory
import loadmap
import Player
import Potentiometer

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")
popsound = pygame.mixer.Sound("textures/hud/pop.wav")
#music = pygame.mixer.Sound("sounds/mix 8bit.wav")
#music.play()
volume = 0.1
#music.set_volume(volume)
m = False
playerLife = 3

gray = pygame.Color(120, 120, 120, 255)
green = pygame.Color(0, 255, 0, 255)
white = pygame.Color(255, 255, 255, 255)
power = 1
xSlider = (650/2) + 50
wRect = 650
slider = Potentiometer.Potentiometer(xSlider, (65/2) + 15, 8, 22, green, 1)

window = pygame.display.set_mode((1024, 768))

def f():
	Menu.Menu.menustate = 0
button1 = Button.Button(380, 300, 250, 70, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 48, "Play", f, -1, -1, 1, -1)
def f():
	exit()
button2 = Button.Button(380, 500, 250, 70, "textures/menu/button.png", "textures/menu/INVASION2000.TTF", 48, "Quit", f, 0, -1, -1, -1)

menu = Menu.Menu([button1, button2], "textures/menu/background/")

currentlevel = 0
maps = []
map_imgs = []
for i in range(2):
	maps.append(Map('textures/tmx/level{}.tmx'.format(i)))
	map_imgs.append(maps[i].make_map())

camera = Camera(0, 0, 500)
loadmap.initMatrix(Entity, maps[0])
dCount = 0

script = "scripts/script.txt"
dialog = Dialog.Dialog(40, script, dCount)
myfont = pygame.font.SysFont("scripts/fonts/VCR_OSD_MONO_1.001.ttf", 27)

heart = []
dark = []
xhearts = 10
for s in range(playerLife):
	heart.append(Hearts.Hearts(xhearts, 10, "heart"))
	dark.append(Hearts.Hearts(xhearts, 10, "dark"))
	xhearts += 50

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
	rect = Potentiometer.Potentiometer(50, 50, wRect, 15, gray, 0)

	if key[pygame.K_ESCAPE]:
		Menu.Menu.menustate = 1

	if Menu.Menu.menustate == 0:
		camera.x = Entity.entities[0].position.x
		camera.y = Entity.entities[0].position.y

		if camera.x - camera.w/2 < 0:
			camera.x = camera.w/2
		if camera.y - camera.h/2 < 0:
			camera.y = camera.h/2
		if camera.x + camera.w/2 > maps[currentlevel].width:
			camera.x = maps[currentlevel].width - camera.w/2
		if camera.y + camera.h/2 > maps[currentlevel].height:
			camera.y = maps[currentlevel].height - camera.h/2

		map_imgs[currentlevel] = pygame.transform.scale(map_imgs[currentlevel], (int(maps[currentlevel].width * 1024 / camera.w), int(maps[currentlevel].height * 1024 / camera.w)))
		posmap = map_imgs[currentlevel].get_rect()

		posmap = posmap.move(int(-camera.x * 1024 / camera.w + 512), int(-camera.y * 1024 / camera.w + 383))
		window.blit(map_imgs[currentlevel], posmap)
		posmap = posmap.move(int(camera.x * 1024 / camera.w - 512), int(camera.y * 1024 / camera.w - 383))

		Entity.entities[0].inventory.box(window)

		if not Entity.entities[0].keyowned:
			if Entity.entities[0].key:
				Entity.entities[0].inventory.addItem(window, "key")
				Entity.entities[0].keyowned = True

		Entity.draw(window, camera)
		result = Entity.collider(window, maps, map_imgs, Entity.entities[0], window, camera, currentlevel)
		if result != -1:
			currentlevel = result

		for i in range(3):
			if i < playerLife:
				heart[i].box(window)
			else:
				dark[i].box(window)

		if playerLife == 0:
			Menu.Menu.menustate = 1
			playerLife = 3
	else:
		Menu.Menu.menus[Menu.Menu.menustate - 1].draw(window)
		rect.draw(window)
		slider.draw(window)
		if key[pygame.K_RIGHT]:
			if xSlider >= wRect + 47:
				xSlider = 700
				volume = 0.2
			else:
				slider.deplacement(window, power)
				xSlider += power
		if key[pygame.K_LEFT]:
			if xSlider <= 50:
				xSlider = 50
				volume = 0
			else:
				slider.deplacement(window, power)
				xSlider -= power

		percentSlide = int((100*(xSlider - 50))/650)
		label = myfont.render(str(percentSlide)+" %", 1, white)
		slvolume = myfont.render("Volume : ", 1, white)
		window.blit(label, (xSlider+10, 49))
		window.blit(slvolume, (300, 20))

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
