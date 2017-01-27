import pygame
from data.constants import *

keyPressed = False

screen.blit(bgImage, (0, 0))
textSurface = introFont.render("oil//water", True, white)

textWidth = textSurface.get_width()
textHeight = textSurface.get_height()
screen.blit(textSurface, ((display_width - textWidth) / 2, (display_height - textHeight) / 2))

while keyPressed == False:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			keyPressed = True
		pygame.display.update()