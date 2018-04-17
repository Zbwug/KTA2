from Entity import Entity
class Player(Entity):
	def __init__(self, x, y, image, nbAnimsFrames, pace):
		super(Player, self).__init__(x, y, image, nbAnimsFrames, pace)

	def render(window):
		super(Player, self).render(window)
		key = pygame.key.get_pressed()
		if key[pygame.K_s]:
			anim = 0
		if key[pygame.K_q]:
			anim = 1
		if key[pygame.K_z]:
			anim = 2
		if key[pygame.K_d]:
			anim = 3
