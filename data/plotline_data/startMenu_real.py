import pygame, sys
 
pygame.init()
display_width = 800
display_height = 500
screen = pygame.display.set_mode((display_width, display_height))
bgImage = pygame.image.load("spacetrees.png")
pygame.display.set_caption('OIL//WATER')
screen.blit(bgImage, (0, 0))

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

class menuItem():
	def __init__(self, text, position, opacity):
		self.text = text
		self.position = position
		self.opacity = opacity
		self.buttonSurface = pygame.Surface((display_width / 3, 50))
		pygame.Surface.convert_alpha(self.buttonSurface)
		self.buttonSurface.set_alpha(self.opacity)
	def setOpacity(self, opacity):
		self.opacity = opacity
		self.buttonSurface.set_alpha(self.opacity)
		pass
class gameMenu():
	def __init__(self, menuItems):
		self.menuItems = menuItems
		menuButtonXPos = 0
		for item in self.menuItems:
			self.position = (menuButtonXPos, display_height / 1.35)
			print item
			print menuItems[item]
			self.m_i = menuItem(item, self.position, 0)
			print "position: " + str(self.m_i.position)
			self.m_i.buttonSurface.fill(white)
			self.m_i.buttonSurface.set_alpha(50)
			screen.blit(self.m_i.buttonSurface, (self.m_i.position))
			menuButtonXPos += self.m_i.buttonSurface.get_width()
	def hoverSelection(self, opacity):
		print "testing hoverSelection."
		self.opacity = opacity
		cur_item = self.m_i.buttonSurface
		cur_item.set_alpha(100)
		screen.blit(cur_item, (self.position))
		pygame.display.update()
	def run(self):
		optionSelected = False
		clock = pygame.time.Clock()
		clock.tick(60)
		self.optionPosition = 0
#		menuItem.buttonSurface.set_alpha(100)
		while optionSelected == False:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
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
							print "optionPosition: " + str(self.optionPosition)
							print "K_d pressed."
					# add change opacity function here
					if self.optionPosition == 0:
						self.hoverSelection(50)
						if key[pygame.K_SPACE]:
							startFunctions["new game"]()
							self.menuRunning = False
					elif self.optionPosition == 1:
						if key[pygame.K_SPACE]:
							startFunctions["load game"]()
							self.menuRunning = False
					elif self.optionPosition == 2:
						if key[pygame.K_SPACE]:
							startFunctions["exit game"]()
							self.menuRunning = False
			pygame.display.update()

def new_game():
	print "starting new game!"
def load_game():
	print "loading old game!"
def exit_game():
	print "exiting game!"
	pygame.quit()
	sys.exit()
			
startFunctions = {"new game" : new_game, "load game" : load_game, "exit game" : exit_game}

gm = gameMenu(startFunctions)
gm.run()