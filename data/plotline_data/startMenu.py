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
screen.fill(white)
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
		for index, item in enumerate(functions):
			print "enumerate: " + str(index) + " : " + item
	def setPosition(self, x, y):
		menuButtonXPos = 0
		yPos = (display_height / 1.35)
		self.position = x, y
	def setOpacity(self, opacity):
		self.opacity = opacity
		self.buttonSurface.set_alpha(self.opacity)
def startMenu():
	menuRunning = True
	optionPosition = 0
	# add menuItem and positioning functions here.
	while menuRunning == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				key = pygame.key.get_pressed()
				if key[pygame.K_a]:
					if 0 < optionPosition <= 2:
						optionPosition -= 1
						print "optionPosition: " + str(optionPosition)
						print "K_a pressed."
				if key[pygame.K_d]:
					if 0 <= optionPosition < 2:
						optionPosition += 1
						print "K_d pressed."
						print "optionPosition: " + str(optionPosition)
				# add change opacity function here
				if key[pygame.K_SPACE]:
					print "option selected."
					if optionPosition == 0:
						startFunctions["new game"]()
					elif optionPosition == 1:
						startFunctions["load game"]()
					elif optionPosition == 2:
						startFunctions["exit game"]()
					menuRunning = False
			
startFunctions = {"new game" : new_game, "load game" : load_game, "exit game" : exit_game}

test_mi = menuItem(startFunctions.keys(), startFunctions, 100)
test_mi.setOpacity(100)
print test_mi.opacity
print startFunctions["new game"]
startMenu()