#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame, sys
from Entity import *

class Inventory:

	def __init__(self, x, y, player):
		self.x = x
		self.y = y
		self.img = pygame.image.load("textures/hud/inventory.png")
		self.img = pygame.transform.scale(self.img, (int(148*1.5), int(39*1.5)))
		self.listOfItems = []
		self.fontDialog = pygame.font.Font("scripts/fonts/font.ttf",30)
		self.full = self.fontDialog.render("L'inventaire est plein !", 1, (255, 0, 0))
		self.full = self.fontDialog.render("L'inventaire est vide !", 1, (0, 255, 0))
		self.keyimg = pygame.image.load("textures/objects/key.png")
		self.keyimg = pygame.transform.scale(self.keyimg, (14*2, 16*2))
		self.player = player

	def box(self, window):
		window.blit(self.img, (self.x, self.y))
		for items in range(len(self.listOfItems)):
			if self.listOfItems[items] == "key":
				window.blit(self.keyimg, ((446, 726)))

	def addItem(self, window, item):
		if len(self.listOfItems) >= 4:
			window.blit(self.full, (self.x, self.y - int(39*1.4)))
		else:
			self.listOfItems.append(item)

	def removeItem(self, window, itemId):
		if len(self.listOfItems) == 0:
			window.blit(self.empty, (self.x, self.y - int(39*1.4)))
		if len(self.listOfItems) > 4:
			return null
