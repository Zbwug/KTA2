import pygame
import sys
sys.path.insert(0, "Menu")
from Button import Button

class Menu:
	menus = []
	menustate = 1

	def __init__(self, buttons, gif):
		self.buttons = buttons
		self.selectedbutton = 0
		self.pressedenterbutton = False
		self.menus.append(self)
		self.gif = gif
		self.img1 = pygame.image.load("textures/menu/background/1.png")
		self.img2 = pygame.image.load("textures/menu/background/2.png")
		self.img3 = pygame.image.load("textures/menu/background/3.png")
		self.img4 = pygame.image.load("textures/menu/background/4.png")
		self.img5 = pygame.image.load("textures/menu/background/5.png")
		self.img6 = pygame.image.load("textures/menu/background/6.png")
		self.img7 = pygame.image.load("textures/menu/background/7.png")
		self.img8 = pygame.image.load("textures/menu/background/8.png")
		self.position1 = self.img1.get_rect()
		self.position2 = self.img2.get_rect()
		self.position3 = self.img3.get_rect()
		self.position4 = self.img4.get_rect()
		self.position5 = self.img5.get_rect()
		self.position6 = self.img6.get_rect()
		self.position7 = self.img7.get_rect()
		self.position8 = self.img8.get_rect()
		
		
		

	def draw(self, window):
		key = pygame.key.get_pressed()
		window.blit(self.img1, self.position1)
		window.blit(self.img2, self.position2)
		window.blit(self.img3, self.position3)
		window.blit(self.img4, self.position4)
		window.blit(self.img5, self.position5)
		window.blit(self.img6, self.position6)
		window.blit(self.img7, self.position7)
		window.blit(self.img8, self.position8)
		for j in range(len(self.buttons)):
			if self.selectedbutton == j:
				if type(self.buttons[j]) is Button:
					if key[pygame.K_RETURN]:
						window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 0 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
						window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + 110, self.buttons[j].position.y - 3))
						pressedenterbutton = True
					else:
						window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 2 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
						window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + 110, self.buttons[j].position.y - 3))
				#if type(self.buttons[j]) is Potentiometer:
				#	window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 1 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
				#	if key[pygame.K_q] and self.buttons[j].level != 0:
				#		self.buttons[j].level -= 1
				#	elif key[pygame.K_d] and self.buttons[j].level != 100:
				#		self.buttons[j].level += 1
			else:
				if type(self.buttons[j]) is Button:
					window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 1 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
					window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + 110, self.buttons[j].position.y - 3))
				#if type(self.buttons[j]) is Potentiometer:
				#	window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 0 * self.buttons[j].size[1] / 3, self.buttons[j].size[0], self.buttons[j].size[1] * 1/3))
				#	window.blit(self.buttons[j].font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + 110, self.buttons[j].position.y - 3))
		if not key[pygame.K_RETURN] and self.pressedenterbutton:
			self.buttons[self.selectedbutton].func()
			pressedenterbutton = False
		if key[pygame.K_LEFT] and self.buttons[self.selectedbutton].q != -1:
			self.selectedbutton = self.buttons[self.selectedbutton].q
		if key[pygame.K_RIGHT] and self.buttons[self.selectedbutton].d != -1:
			self.selectedbutton = self.buttons[self.selectedbutton].d
		if key[pygame.K_UP] and self.buttons[self.selectedbutton].z != -1:
			self.selectedbutton = self.buttons[self.selectedbutton].z
		if key[pygame.K_DOWN] and self.buttons[self.selectedbutton].s != -1:
			self.selectedbutton = self.buttons[self.selectedbutton].s
		self.pressedenterbutton = key[pygame.K_RETURN]
		

		 

