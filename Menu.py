import pygame, sys, time
sys.path.insert(0, "Menu")
from Button import Button

class Menu:
	menus = []
	menustate = 1
	down = False
	up = False

	def __init__(self, buttons, gif):
		self.buttons = buttons
		self.selectedbutton = 0
		self.pressedenterbutton = False
		self.menus.append(self)
		self.gif = gif
		self.gifbg = pygame.image.load("textures/menu/background/gif2.png")
		self.gifbg =  pygame.transform.scale(self.gifbg, (8192, 768))
		self.logo = pygame.image.load("textures/menu/logo.png")
		self.logo = pygame.transform.scale(self.logo, (555, 408))
		self.logoposition = self.logo.get_rect()
		self.gifposition = self.gifbg.get_rect()
		self.maxNumberOfFrame = 8
		self.cdGif = 0
		self.temp = 0

	def draw(self, window):
		key = pygame.key.get_pressed()
		self.temp = (self.temp + 1) % 10
		if self.temp == 9:
			self.cdGif = (self.cdGif + 1) % (self.maxNumberOfFrame - 1)
		window.blit(self.gifbg, self.gifposition, (self.cdGif*1024, 0, 1024, 768))
		window.blit(self.logo, self.logoposition, (-250, 0, 1024, 768))

		for j in range(len(self.buttons)):
			if self.selectedbutton == j:
				if type(self.buttons[j]) is Button:
					if key[pygame.K_RETURN]:
						window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 0 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
						window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + self.buttons[j].xbutton, self.buttons[j].position.y + 7))
						pressedenterbutton = True
					else:
						window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 2 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
						window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + self.buttons[j].xbutton, self.buttons[j].position.y + 7))
			else:
				if type(self.buttons[j]) is Button:
					window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 1 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
					window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + self.buttons[j].xbutton, self.buttons[j].position.y + 7))

		if not key[pygame.K_RETURN] and self.pressedenterbutton:
			self.buttons[self.selectedbutton].func()
			pressedenterbutton = False
		
		if not Menu.down and not Menu.up:	
			if key[pygame.K_LEFT] and self.buttons[self.selectedbutton].q != -1:
				self.selectedbutton = self.buttons[self.selectedbutton].q
			if key[pygame.K_RIGHT] and self.buttons[self.selectedbutton].d != -1:
				self.selectedbutton = self.buttons[self.selectedbutton].d
			if key[pygame.K_UP] and self.buttons[self.selectedbutton].z != -1:
				self.selectedbutton = self.buttons[self.selectedbutton].z
				Menu.up = True
			if key[pygame.K_DOWN] and self.buttons[self.selectedbutton].s != -1:
				self.selectedbutton = self.buttons[self.selectedbutton].s
				Menu.down = True
		self.pressedenterbutton = key[pygame.K_RETURN]
