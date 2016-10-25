import sys, pygame, OpenGL

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
display_width = 800
display_height = 500
screen = pygame.display.set_mode((display_width, display_height))
bgImage = pygame.image.load("spacetrees.png")

trans = pygame.Surface((300, 500))
trans.fill(black)
pygame.Surface.convert_alpha(trans)
trans.set_alpha(50)
screen.blit(bgImage, (0,0))
screen.blit(trans, ((display_width - 300) / 2, 0))

def gameLoop():
	gameRunning = True
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			pygame.quit()
			sys.exit()
		pygame.display.update()

gameLoop()