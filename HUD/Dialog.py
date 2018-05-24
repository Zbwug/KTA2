#!/usr/bin/env python
#-*- coding: utf-8 -*-
import pygame, sys, linecache

class Dialog:

	def __init__(self, x, script, dCount):
		self.x = x
		self.textbox = pygame.image.load("textures/hud/textbox.png")
		self.textbox = pygame.transform.scale(self.textbox, (1020, 200))
		self.fontDialog = pygame.font.Font("scripts/fonts/font.ttf",30)
		self.script = script
		self.txt = self.fontDialog.render(self.getLine(dCount), 1, (0, 0, 0))


	def box(self, window):
		window.blit(self.textbox, (0, 568))
		window.blit(self.txt, (self.x, 768-(200/2)))

	def getLine(self, n):
		script = open(self.script, "r")
		str = script.read()
		count = 0
		result = ""
		chr = "\n"
		for i in range(len(str)):
			if str[i] == chr:
				count += 1
			if count == n and str[i] != chr:
				result += str[i]
			if count - 1 == n:
				return result

	def maxLines(self):
		script = open(self.script, "r")
		str = script.read()
		count = 0
		chr = "\n"
		for i in range(len(str)):
			if str[i] == chr:
				count += 1
		return count + 1
