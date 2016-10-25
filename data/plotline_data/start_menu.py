import sys, pygame, OpenGL

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
display_width = 800
display_height = 500
screen = pygame.display.set_mode((display_width, display_height))
bgImage = pygame.image.load("spacetrees.png")

mainMenu = pygame.Surface((300, 500))
mainMenu.fill(white)
pygame.Surface.convert_alpha(mainMenu)
mainMenu.set_alpha(50)
# screen.blit(bgImage, (0,0))
screen.blit(mainMenu, ((display_width - 300) / 2, 0))

selectionPos = 0
# write something so that if selectionPos = 0
# change the appearence of the menu item you're hovered over

# white something so that if you hit the up arrow the selectionPos
# variable += or -= 1

# also, to stop loop from continuing to run, create a variable within
# loop that will stop when posChanged == true or something like that.

def gameLoop():
	gameRunning = True
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			pygame.quit()
			sys.exit()
		pygame.display.update()

gameLoop()