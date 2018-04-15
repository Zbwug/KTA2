class Menu:
	menus = []
	menustate = 0
    
	def __init__(self, buttons):
		self.buttons = buttons
		self.selectedbutton = 0
		self.pressedenterbutton = False
        menus.append(self)
    
	def draw(window):
		key = pygame.key.get_pressed()
		for j in range(len(buttons)):
			if selectedbutton == j:
				if type(buttons[j]) is Button:
					if key[pygame.K_RETURN]:
						window.blit(buttons[j].sprite, buttons[j].position, (0, 0 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
						pressedenterbutton = True
					else:
						window.blit(buttons[j].sprite, buttons[j].position, (0, 2 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
				if type(buttons[j]) is Potentiometer:
					window.blit(buttons[j].sprite, buttons[j].position, (0, 1 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
					if key[pygame.K_q] && buttons[j].level != 0:
						buttons[j].level -= 1 
					else if key[pygame.K_d] && buttons[j].level != 100:
						buttons[j].level += 1
			else:
				if type(buttons[j]) is Button:
					window.blit(buttons[j].sprite, buttons[j].position, (0, 1 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
					window.blit(font.render(buttons[j].text, 1, (200, 200, 200)), (buttons[j].position.x + 110, buttons[j].position.y - 3))
				if type(buttons[j]) is Potentiometer:
					window.blit(buttons[j].sprite, buttons[j].position, (0, 0 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
					window.blit(font.render(buttons[j].text, 1, (200, 200, 200)), (buttons[j].position.x + 110, buttons[j].position.y - 3))
		if not key[pygame.K_RETURN] and pressedenterbutton:
			buttons[selectedbutton].func()
			pressedenterbutton = False
		if key[pygame.K_LEFT] and buttons[selectedbutton].q != -1:
			selectedbutton = buttons[selectedbutton].q
		if key[pygame.K_RIGHT] and buttons[selectedbutton].d != -1:
			selectedbutton = buttons[selectedbutton].d
		if key[pygame.K_UP] and buttons[selectedbutton].z != -1:
			selectedbutton = buttons[selectedbutton].z
		if key[pygame.K_DOWN] and buttons[selectedbutton].s != -1:
			selectedbutton = buttons[selectedbutton].s
