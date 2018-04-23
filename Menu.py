import pygame

class Menu:
	menus = []
	menustate = 1
	
	def __init__(self, buttons):
		self.buttons = buttons
		self.selectedbutton = 0
		self.pressedenterbutton = False
		self.menus.append(self)
    
	def draw(self, window):
		key = pygame.key.get_pressed()
		for j in range(len(self.buttons)):
			if selectedbutton == j:
				if type(self.buttons[j]) is Button:
					if key[pygame.K_RETURN]:
						window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 0 * self.buttons[j].spriteSize[1] / 3, self.buttons[j].spriteSize[0], self.buttons[j].spriteSize[1] * 1/3))
						pressedenterbutton = True
					else:
						window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 2 * self.buttons[j].spriteSize[1] / 3, self.buttons[j].spriteSize[0], self.buttons[j].spriteSize[1] * 1/3))
				if type(self.buttons[j]) is Potentiometer:
					window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 1 * self.buttons[j].spriteSize[1] / 3, self.buttons[j].spriteSize[0], self.buttons[j].spriteSize[1] * 1/3))
					if key[pygame.K_q] and self.buttons[j].level != 0:
						self.buttons[j].level -= 1 
					elif key[pygame.K_d] and self.buttons[j].level != 100:
						self.buttons[j].level += 1
			else:
				if type(self.buttons[j]) is Button:
					window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 1 * self.buttons[j].spriteSize[1] / 3, self.buttons[j].spriteSize[0], self.buttons[j].spriteSize[1] * 1/3))
					window.blit(font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + 110, self.buttons[j].position.y - 3))
				if type(self.buttons[j]) is Potentiometer:
					window.blit(self.buttons[j].sprite, self.buttons[j].position, (0, 0 * self.buttons[j].spriteSize[1] / 3, self.buttons[j].spriteSize[0], self.buttons[j].spriteSize[1] * 1/3))
					window.blit(font.render(self.buttons[j].text, 1, (200, 200, 200)), (self.buttons[j].position.x + 110, self.buttons[j].position.y - 3))
		if not key[pygame.K_RETURN] and pressedenterbutton:
			self.buttons[selectedbutton].func()
			pressedenterbutton = False
		if key[pygame.K_LEFT] and self.buttons[selectedbutton].q != -1:
			selectedbutton = self.buttons[selectedbutton].q
		if key[pygame.K_RIGHT] and self.buttons[selectedbutton].d != -1:
			selectedbutton = self.buttons[selectedbutton].d
		if key[pygame.K_UP] and self.buttons[selectedbutton].z != -1:
			selectedbutton = self.buttons[selectedbutton].z
		if key[pygame.K_DOWN] and self.buttons[selectedbutton].s != -1:
			selectedbutton = self.buttons[selectedbutton].s
