import pygame, sys, linecache

class Dialog:

	def __init__(self, x, script, dCount):
		self.x = x
		self.textbox = pygame.image.load("textures/hud/textbox.png")
		self.textbox = pygame.transform.scale(self.textbox, (1020, 200))
		self.fontDialog = pygame.font.Font(None,30)
		self.script = script
		self.txt = self.fontDialog.render(self.getLine(dCount).rstrip("\n"), 1, (0, 0, 0))


	def box(self, window):
		window.blit(self.textbox, (0, 568))
		window.blit(self.txt, (self.x, 768-(200/2)))

	def getNumberOfLines(self):
		script = open(self.script, "r")
		n = 0
		for lines in script:
			n += 1
		return n

	def getLine(self, n):
		return linecache.getline(self.script, n)
		
