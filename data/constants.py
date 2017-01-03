import pygame, sys
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

clock = pygame.time.Clock()

display_width = 800
display_height = 400

#def createDisplay():
pygame.init()
window = pygame.display.set_mode((display_width, display_height), HWSURFACE | OPENGL | DOUBLEBUF)
pygame.display.set_caption('OIL//WATER')
glViewport(0, 0, display_width, display_height)
	
def updateDisplay():
	clock.tick(60)
	pygame.display.flip()
	
def closeDisplay():
	pygame.quit()
	sys.exit()

# game loop to keep the game running.
def gameLoop():
	gameRunning = True
	createDisplay()
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			closeDisplay()
		updateDisplay()


screen = pygame.Surface((display_width, display_height), SRCALPHA)
screenFire = pygame.Surface((display_width, display_height), SRCALPHA)

bgImage = pygame.image.load("spacetrees.png")


lineFont = pygame.font.Font("freesansbold.ttf", 10)
menuLabelFont = pygame.font.Font("freesansbold.ttf", 15)
introFont = pygame.font.Font("freesansbold.ttf", 20)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()

#glOrtho(0, display_width, display_height, 0, -1, 1000.0)
gluPerspective(45.0, float(display_width) / display_height, 0.0, 1000.0)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

glEnable(GL_TEXTURE_2D)
glDisable(GL_CULL_FACE)
glClearColor(0, 0, 0, 0)
glTranslatef(-(display_width / 2), -(display_height / 2), -488)

glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #| GL_DEPTH_BUFFER_BIT)

def convertSurface(surface):
	#generate opengl texture from surface.
	bbuffer_tex = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, bbuffer_tex)

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
	glEnable(GL_BLEND)
	glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
	tex_data = pygame.image.tostring(surface, "RGBA", True)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, display_width, display_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_data)
	#start drawing texture.
	glBindTexture(GL_TEXTURE_2D, bbuffer_tex)
	#finish drawing texture.
	glClear(GL_DEPTH_BUFFER_BIT)

	tex_data = pygame.image.tostring(surface, "RGBA", False)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, display_width, display_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_data)
	
	glBegin(GL_QUADS)

	glTexCoord2i(0, 1)
	glVertex3f(0.0, 0.0, -10.0)

	glTexCoord2i(1, 1)
	glVertex3f(display_width, 0.0, -10.0)

	glTexCoord2i(1, 0)
	glVertex3f(display_width, display_height, -10.0)

	glTexCoord2i(0, 0)
	glVertex3f(0.0, display_height, -10.0)
	glEnd()
#show the updated frame.
	pygame.display.flip()
	glDeleteTextures(1)

