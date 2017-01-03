import sys
from data.constants import *

def testCube():
	pass

def runIntro():
	print "run intro."
	keyPressed = False
	while keyPressed == False:
		screen.blit(bgImage, (0, 0))
		textSurface = introFont.render("oil//water", True, white)
		screen.blit(textSurface, ((display_width - textSurface.get_width()) / 2, (display_height - textSurface.get_height()) / 2))
		convertSurface(screen)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				keyPressed = True