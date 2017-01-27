import pygame, sys
from data.constants import *

screen.blit(bgImage, (0, 0))

class menuItem():
	def __init__(self, itemLabel, itemPosition, itemOpacity, itemID):
		self.itemLabel = itemLabel
		self.itemLabelSurface = menuLabelFont.render(self.itemLabel, True, white)
		self.itemPosition = itemPosition
		self.itemOpacity = itemOpacity
		self.itemID = itemID
		self.itemSurface = pygame.Surface((display_width / 3, 50)) #see about using len(menuItems) instead of "3" later.
		pygame.Surface.convert_alpha(self.itemSurface)
class gameMenu():
	def __init__(self, menuItems):
		self.menuItems = menuItems
		self.itemIDIncrement = 0
		self.itemXPos = 0
		self.items = []
		self.opacity = 0
	def drawMenu(self):
		screen.blit(bgImage, (0, 0))
		for item in self.menuItems:
			m_i = "m_"
			m_i += str(self.itemIDIncrement)
			self.items.append(m_i)
			self.items[self.itemIDIncrement] = menuItem(item, (self.itemXPos, int(display_height / 1.35)), 50, self.itemIDIncrement)
			self.items[self.itemIDIncrement].itemSurface.fill(white)
			self.items[self.itemIDIncrement].itemSurface.set_alpha(self.opacity)
			screen.blit(self.items[self.itemIDIncrement].itemLabelSurface, self.items[self.itemIDIncrement].itemPosition)
			screen.blit(self.items[self.itemIDIncrement].itemSurface, self.items[self.itemIDIncrement].itemPosition)
			self.itemXPos += (self.items[self.itemIDIncrement].itemSurface.get_width()) + 1
			self.itemIDIncrement += 1
		print self.items[2].itemLabel + " position: " + str(self.items[2].itemPosition)
	def setHoverOpacity(self, opacity, curPosition):
		self.opacity = opacity
		self.curPosition = curPosition
		if self.curPosition == 0:
			print "current position: 0"
			self.items[0].itemSurface.set_alpha(50)
			screen.blit(self.items[0].itemSurface, self.items[0].itemPosition)
		elif self.curPosition == 1:
			print "current position: 1"
			self.items[1].itemSurface.set_alpha(50)
			screen.blit(self.items[1].itemSurface, self.items[1].itemPosition)
		elif self.curPosition == 2:
			print "current position: 2"
			self.items[2].itemSurface.set_alpha(50)
			screen.blit(self.items[2].itemSurface, self.items[2].itemPosition)
		for index, item in enumerate(self.menuItems):
			screen.blit(self.items[index].itemLabelSurface, self.items[index].itemPosition)
	def run(self):
		self.optionSelected = False
		clock = pygame.time.Clock()
		clock.tick(60)
		self.optionPosition = 0
		self.drawMenu()
		while self.optionSelected == False:
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
					if self.optionPosition == 0:
						self.drawMenu()
						self.setHoverOpacity(50, 0)
						if key[pygame.K_SPACE]:
							startFunctions["new game"]()
							self.optionSelected = True
							screen.blit(bgImage, (0, 0))
					elif self.optionPosition == 1:
						self.drawMenu()
						self.setHoverOpacity(50, 1)
						if key[pygame.K_SPACE]:
							startFunctions["load game"]()
					elif self.optionPosition == 2:
						self.drawMenu()
						self.setHoverOpacity(50, 2)
						if key[pygame.K_SPACE]:
							startFunctions["exit game"]()
							self.optionSelected = True
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