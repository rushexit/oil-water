import sys, pygame

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

# need a class for menuOptions
class menuOptions(object):
	def __init__(self, menuLabel, isSelected, menuPosition):
		self.menuLabel = menuLabel
		self.isSelected = isSelected
		self.menuPosition = menuPosition
	def setPos(self, xCoord, yCoord):
		self.position = (xCoord, yCoord)
zebra = menuOptions("startNewGame", False, 0)
print zebra.menuPosition
print zebra.menuLabel
print zebra.isSelected
