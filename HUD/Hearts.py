#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame, sys

class Hearts:

	def __init__(self, x, y, state):
		self.x = x
		self.y = y
		self.state = state
		self.heart = pygame.image.load("textures/hud/hearts.png")
		self.dark = pygame.image.load("textures/hud/dark.png")
		self.fontDialog = pygame.font.Font("scripts/fonts/font.ttf",30)

	def box(self, window):
		if self.state == "heart":
			window.blit(self.heart, (self.x, self.y))
		if self.state == "dark":
			window.blit(self.dark, (self.x, self.y))
