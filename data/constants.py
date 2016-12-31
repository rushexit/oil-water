import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

print "constants imported."
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

display_width = 800
display_height = 400
window = pygame.display.set_mode((display_width, display_height), HWSURFACE | OPENGL | DOUBLEBUF)
screen = pygame.Surface((display_width, display_height))
pygame.display.set_caption('OIL//WATER')
bgImage = pygame.image.load("spacetrees.png")

lineFont = pygame.font.Font("freesansbold.ttf", 10)
menuLabelFont = pygame.font.Font("freesansbold.ttf", 15)
introFont = pygame.font.Font("freesansbold.ttf", 20)

glEnable(GL_TEXTURE_2D)
glClearColor(0, 0, 0, 0)

glViewport(0, 0, display_width, display_height)

glClear(GL_COLOR_BUFFER_BIT)

glMatrixMode(GL_PROJECTION)
glLoadIdentity()

glOrtho(0, display_width, display_height, 0, -1, 1)

glMatrixMode(GL_MODELVIEW)
glLoadIdentity()

def convertSurface(surface):
	#generate opengl texture from surface.
	bbuffer_tex = glGenTextures(1)
	glBindTexture(GL_TEXTURE_2D, bbuffer_tex)

	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
	glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

	tex_data = pygame.image.tostring(surface, "RGBA", 1)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, display_width, display_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_data)
	#start drawing texture.
	glBindTexture(GL_TEXTURE_2D, bbuffer_tex)
#	surface.fill(pygame.Color('black'))
	#finish drawing texture.
	glClear(GL_DEPTH_BUFFER_BIT)

	tex_data = pygame.image.tostring(surface, "RGBA", 1)
	glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, display_width, display_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_data)
	
	glBegin(GL_QUADS)

	glTexCoord2i(0, 1)
	glVertex2f(0, 0)

	glTexCoord2i(1, 1)
	glVertex2f(display_width, 0)

	glTexCoord2i(1, 0)
	glVertex2f(display_width, display_height)

	glTexCoord2i(0, 0)
	glVertex2f(0, display_height)
	glEnd()
#show the updated frame.
	pygame.display.flip()
	glDeleteTextures(1)