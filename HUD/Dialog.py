import pygame, sys, linecache

class Dialog:
	
	
	def __init__(self, x, txt):
		self.x = x
		self.textbox = pygame.image.load("textures/hud/textbox.png")
		self.textbox = pygame.transform.scale(self.textbox, (1020, 200))
		self.fontDialog = pygame.font.Font(None,30)
		self.txt = self.fontDialog.render(txt, 1, (0, 0, 0))


		
	def box(self, window):
		window.blit(self.textbox, (0, 568))
		window.blit(self.txt, (self.x, 768-(200/2)))
		
	def getNumberOfLines():
		n = 0
		script = open("textures/hud/script.txt", "r")
		for file in script:
			n += 1
		return n
	
	def getLine(n):
		script = "textures/hud/script.txt"
		return linecache.getline(script, n)
		
		

        

		
