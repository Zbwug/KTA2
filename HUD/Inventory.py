#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame, sys

class Inventory:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.img = pygame.image.load("textures/hud/inventory.png")
		self.img = pygame.transform.scale(self.img, (int(148*1.5), int(39*1.5)))
		self.listOfItems = items[]
		self.fontDialog = pygame.font.Font(None,30)
		self.full = self.fontDialog.render("L'inventaire est plein !", 1, (255, 0, 0))
		self.full = self.fontDialog.render("L'inventaire est vide !", 1, (0, 255, 0))
		
		
	def box(self, window):
		window.blit(self.img, (self.x, self.y))	
		
	def addItem(self, window, itemId):
		if len(self.listOfItems) < 0:
			return null
		if len(self.listOfItems) >= 4:
			window.blit(self.full, (self.x, self.y - int(39*1.4)))
		else:
			#TODO
		
	def removeItem(self, window, itemId):
		if len(self.listOfItems) <= 0:
			window.blit(self.empty, (self.x, self.y - int(39*1.4)))
		if len(self.listOfItems) > 4:
			return null
		if len(self.listOfItems) <= 4:
			#TODO
			
	def showItems(self, )
		
			
		
		
		
