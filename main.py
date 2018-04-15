import pygame, pytmx, math, copy
from pygame.locals import *
from 'Map.py' include *

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Kill the Anthony 2")

fenetre = pygame.display.set_mode((1600, 900))
clock = pygame.time.Clock()

windowOpen = True
while windowOpen:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
  key = pygame.key.get_pressed()
	
  if menustate == 0:
    for j in range(len(buttons)):
      if selectedbutton == j:
        if key[pygame.K_RETURN]:
          fenetre.blit(buttons[j].sprite, buttons[j].position, (0, 0 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
          pressedenterbutton = True
        else:
          fenetre.blit(buttons[j].sprite, buttons[j].position, (0, 2 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
      else:
        fenetre.blit(buttons[j].sprite, buttons[j].position, (0, 1 * buttons[j].spriteSize[1] / 3, buttons[j].spriteSize[0], buttons[j].spriteSize[1] * 1/3))
      fenetre.blit(font.render(buttons[j].text, 1, (200, 200, 200)), (buttons[j].position.x + 110, buttons[j].position.y - 3))
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
  if menustate == 1:
	  print("à faire")
	
  if menustate == 2:
    while len(todraw) != 0:
      imin = -1
      ymin = 10000000000000
      for k in range(len(todraw)):
        if todraw[k][0].position.y < ymin:
          imin = k
          ymin = todraw[k][0].position.y
      fenetre.blit(todraw[imin][0].sprite, todraw[imin][0].position, todraw[imin][1])
      todraw.remove(todraw[imin])
    temp = (temp + 1) % 10
    if temp == 0:
      walk = (walk + 1) % 10
  pygame.display.flip()
