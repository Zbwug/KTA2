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
volume = 0.1
mMenu = pygame.mixer.Sound("sounds/mMenu.wav")
mWind = pygame.mixer.Sound("sounds/mWind.wav")
mWood = pygame.mixer.Sound("sounds/mWood.wav")
mBoss = pygame.mixer.Sound("sounds/mBoss.wav")

gray = pygame.Color(120, 120, 120, 255)
green = pygame.Color(0, 255, 0, 255)
white = pygame.Color(255, 255, 255, 255)
power = 1
xSlider = (650/2) + 50
wRect = 650
hRect = 20
xrectslider = 1024/2 - wRect/2
yrectslider = 450
xSlider = (wRect/2) + xrectslider
slider = Potentiometer.Potentiometer(xSlider, yrectslider - 1, 8, 22, "textures/menu/slider.png", "Rectangle")

window = pygame.display.set_mode((1024, 768))

def f():
	Menu.Menu.menustate = 0
button1 = Button.Button(380, 420, 250, 70, "textures/menu/button.png", "scripts/fonts/font.ttf", 48, "Play", f, -1, -1, 1, -1, 60)

def f():
	Menu.Menu.menustate = 2
button2 = Button.Button(380, 540, 250, 70, "textures/menu/button.png", "scripts/fonts/font.ttf", 48, "Options", f, 0, -1, 2, -1, 28)

def f():
	exit()
button3 = Button.Button(380, 660, 250, 70, "textures/menu/button.png", "scripts/fonts/font.ttf", 48, "Quit", f, 1, -1, -1, -1, 67)

def f():
	Menu.Menu.menustate = 1
button4 = Button.Button(380, 600, 250, 70, "textures/menu/button.png", "scripts/fonts/font.ttf", 48, "Quit", f, -1, -1, -1, -1, 67)

Menu.Menu([button1, button2, button3], "textures/menu/background/")
Menu.Menu([button4], "textures/menu/background/")

currentlevel = 0
maps = []
map_imgs = []
for i in range(3):
	maps.append(Map('textures/tmx/level{}.tmx'.format(i)))
	map_imgs.append(maps[i].make_map())

camera = Camera(currentlevel)
loadmap.initMatrix(Entity, window, maps[currentlevel], False, 0)
dCount = 0

script = "scripts/script.txt"
dialog = Dialog.Dialog(40, script, dCount)
myfont = pygame.font.Font("scripts/fonts/font.ttf", 27)

heart = []
dark = []
xhearts = 10

for s in range(Entity.entities[0].life):
	heart.append(Hearts.Hearts(xhearts, 10, "heart"))
	dark.append(Hearts.Hearts(xhearts, 10, "dark"))
	xhearts += 50

clock = pygame.time.Clock()
mMenu.play(loops=-1)

windowOpen = True
while windowOpen:
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				if Menu.Menu.menustate == 1:
					Menu.Menu.down = False
			if event.key == pygame.K_UP:
				if Menu.Menu.menustate == 1:
					Menu.Menu.up = False
	mMenu.set_volume(volume)
	mWind.set_volume(volume)
	mWood.set_volume(volume)
	mBoss.set_volume(volume)
	key = pygame.key.get_pressed()
	rect = Potentiometer.Potentiometer(xrectslider, yrectslider, wRect, hRect, "textures/menu/stone.png", "Rectangle")

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

		if currentlevel == 0 and mWind.get_num_channels() == 0:
			mWood.stop()
			mMenu.stop()
			mBoss.stop()
			mWind.play(loops =-1)
		if currentlevel == 1 and mWood.get_num_channels() == 0:
			mMenu.stop()
			mWind.stop()
			mBoss.stop()
			mWood.play(loops =-1)
		if currentlevel == 2 and mBoss.get_num_channels() == 0:
			mMenu.stop()
			mWind.stop()
			mWood.stop()
			mBoss.play(loops = -1)

		map_imgs[currentlevel] = pygame.transform.scale(map_imgs[currentlevel], (int(maps[currentlevel].width * 1024 / camera.w), int(maps[currentlevel].height * 1024 / camera.w)))
		posmap = map_imgs[currentlevel].get_rect()

		posmap = posmap.move(int(-camera.x * 1024 / camera.w + 512), int(-camera.y * 1024 / camera.w + 383))
		window.blit(map_imgs[currentlevel], posmap)
		posmap = posmap.move(int(camera.x * 1024 / camera.w - 512), int(camera.y * 1024 / camera.w - 383))

		if not Entity.entities[0].keyowned:
			if Entity.entities[0].key:
				Entity.entities[0].inventory.addItem(window, "key")
				Entity.entities[0].keyowned = True

		Entity.draw(window, camera)
		result = Entity.collider(window, maps, map_imgs, Entity.entities[0], camera, currentlevel)
		if result[0] != -1:
			currentlevel = result[0]
		if result[1] != None:
			camera = result[1]

		Entity.entities[0].inventory.box(window)

		for i in range(3):
			if i < Entity.entities[0].life:
				heart[i].box(window)
			else:
				dark[i].box(window)

		if Entity.entities[0].life == 0:
			Menu.Menu.menustate = 1
			Entity.entities[0].life = 3
	else:
		Menu.Menu.menus[Menu.Menu.menustate - 1].draw(window)

	if Menu.Menu.menustate == 2:
		rect.draw(window)
		slider.draw(window)
		if key[pygame.K_RIGHT]:
			if xSlider >= wRect + (xrectslider - 3):
				xSlider = wRect + xrectslider
				volume = 0.2
			elif (xSlider + 512) % 5 == 0:
				volume += 0.002
				slider.deplacement(window, power)
				xSlider += power
			else:
				slider.deplacement(window, power)
				xSlider += power
		if key[pygame.K_LEFT]:
			if xSlider <= xrectslider:
				xSlider = xrectslider
				volume = 0
			elif (xSlider - 512) % 5 == 0:
				volume -= 0.002
				slider.deplacement(window, power)
				xSlider -= power
			else:
				slider.deplacement(window, power)
				xSlider -= power

		percentSlide = int((100*(xSlider - xrectslider))/wRect)
		label = myfont.render(str(percentSlide)+" %", 1, white)
		slvolume = myfont.render("Volume : ", 1, white)
		window.blit(label, (xSlider+10, yrectslider))
		window.blit(slvolume, ((wRect/2) + 0.75*xrectslider, yrectslider - hRect - 30))

	pygame.display.flip()
	clock.tick(144)
