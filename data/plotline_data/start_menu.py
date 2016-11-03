import sys, pygame, OpenGL

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
display_width = 800
display_height = 500
screen = pygame.display.set_mode((display_width, display_height))
bgImage = pygame.image.load("spacetrees.png")
menuButtonAdjust = 0
mainMenu = pygame.Surface((800, 50))
mainMenu.fill(white)
newGameButton = pygame.Surface((display_width /3 , 50))
newGameButton.fill(white)
loadGameButton = pygame.Surface((display_width / 3, 50))
loadGameButton.fill(red)
exitButton = pygame.Surface((display_width / 3, 50))
exitButton.fill(white)
pygame.Surface.convert_alpha(mainMenu)
mainMenu.set_alpha(50)
# screen.blit(bgImage, (0,0))
# screen.blit(mainMenu, (0, (display_height / 1.35)))
# screen.blit(newGameButton, (menuButtonAdjust, (display_height/ 1.35)))
# menuButtonAdjust += newGameButton.get_width()
#screen.blit(loadGameButton, (menuButtonAdjust, (display_height/ 1.35)))
# menuButtonAdjust += exitButton.get_width()
# screen.blit(exitButton, (menuButtonAdjust, (display_height/ 1.35)))

selectionPos = 0

class mainMenuButtons:
	def __init__(self):
		global menuButtonAdjust
		self.Button = pygame.Surface((display_width / 3 , 50))
		self.Button.fill(white)
		pygame.Surface.convert_alpha(self.Button)
		self.Button.set_alpha(50)
		screen.blit(self.Button, (menuButtonAdjust, (display_height / 1.35)))
		menuButtonAdjust += self.Button.get_width()

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

newGameButton = mainMenuButtons()
loadGameButton = mainMenuButtons()
exitButton = mainMenuButtons()
gameLoop()