import pygame, sys

class Dialog:
	def __init__(self, x, txt):
		self.x = x
		self.textbox = pygame.image.load("textures/hud/textbox.png")
		self.textbox = pygame.transform.scale(self.textbox, (1020, 200))
		self.fontDialog = pygame.font.Font(None,30)
		self.txt = self.fontDialog.render(txt, 1, (0, 0, 0))
		self.popsound = pygame.mixer.Sound("textures/hud/pop.wav")

	def box(self, window):
		window.blit(self.textbox, (0, 568))
		window.blit(self.txt, (self.x, 768-(200/2)))
		self.popsound.play()
