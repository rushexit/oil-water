import pygame, sys
#constant variables
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
display_width = 800
display_height = 500

font = pygame.font.Font("freesansbold.ttf", 10)
screen = pygame.display.set_mode((display_width, display_height))
screen.fill(black)
pygame.display.set_caption('OIL//WATER')
pygame.display.update()
def new_game():
	print "starting new game!"
def load_game():
	print "loading old game!"
def exit_game():
	print "exiting game!"
	pygame.quit()
	sys.exit()

#class menuItem(text, functions, choice, opacity):
class menuItem():
	def __init__(self, text, functions, opacity):
		self.text = text
		self.functions = functions
		self.opacity = opacity
		self.buttonSurface = pygame.Surface((display_width / 3, 50))
		self.buttonSurface = self.buttonSurface.convert_alpha()
		self.buttonSurface.fill(white)
		print "text: " + str(text)
#		for index, item in enumerate(functions):
#			print "enumerate: " + str(index) + " : " + item
	def setPosition(self, x, y):
		yPos = (display_height / 1.35)
		self.position = x, y
	def setOpacity(self, opacity):
		self.opacity = opacity
		self.buttonSurface.set_alpha(self.opacity)

class startMenu():
	def __init__(self, functions):
		self.menuRunning = True
		self.optionPosition = 0
		defaultOpacity = 0
		menuButtonXPos = 0
		for item in functions:
			print "do this do that."
			print item
			menuButton = menuItem(item, functions[item], defaultOpacity)
			menuButton.setPosition(menuButtonXPos, 0)
			screen.blit(menuButton.buttonSurface, menuButton.position)
			menuButtonXPos += menuButton.buttonSurface.get_width()
			
	def run(self):
		while self.menuRunning == True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					key = pygame.key.get_pressed()
					if key[pygame.K_a]:
						if 0 < self.optionPosition <= 2:
							self.optionPosition -= 1
							print "optionPosition: " + str(self.optionPosition)
							print "K_a pressed."
					if key[pygame.K_d]:
						if 0 <= self.optionPosition < 2:
							self.optionPosition += 1
							print "K_d pressed."
							print "optionPosition: " + str(self.optionPosition)
					# add change opacity function here
					if self.optionPosition == 0:
						self.menuButton.setOpacity(100)
						if key[pygame.K_SPACE]:
							startFunctions["new game"]()
							self.menuRunning = False
					elif self.optionPosition == 1:
						self.menuButton.setOpacity(100)
						if key[pygame.K_SPACE]:
							startFunctions["load game"]()
							self.menuRunning = False
					elif self.optionPosition == 2:
						self.menuButton.setOpacity(100)
						if key[pygame.K_SPACE]:
							startFunctions["exit game"]()
							self.menuRunning = False

startFunctions = {"new game" : new_game, "load game" : load_game, "exit game" : exit_game}

print startFunctions["new game"]
sm = startMenu(startFunctions)
sm.run()