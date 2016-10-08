import pygame, sys, time, random
from pygame.locals import *

# constant variables & pygame initialization
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
display_width = 800
display_height = 500
font = pygame.font.Font("freesansbold.ttf", 10)
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('OIL//WATER')
screen.fill(white)

gameRunning = True

# game loop to keep game open and running.
def gameLoop():
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			pygame.quit()
			sys.exit()
		pygame.display.update()

# npc_line_reading function, takes current line and blits it to the screen character by character normally.
def npc_line_reading(text):
	line = ''
	currentCharacter = 0
	keyPressed = False
	beatStart = time.time()
	beatTime = 0
	for character in range(len):
		if pygame.event.get(pygame.KEYDOWN):
			keyPressed = True
			line += "--"
			text_surface = font.render(line, True, red)
			screen.blit(text_surface, text_rect)
			pygame.display.update()
			break
		elif keyPressed = False:
			line += text[character]
			currentCharacter += 1
			text_surface = font.render(line, True, black)
			text_rect = text_surface.get_rect()
			
			
# playing_line_reading function,
def player_line_reading(text):

# npc_strange_line_reading fucntion,
def npc_strange_line_reading(text):

# scriptHandler function, imports script text files, reads lines, moves through lines until stopped.
def scriptHandler(scriptFile):
	script = open(scriptFile, 'r')						# imports script text file.
	scriptData = script.readlines()						# reads the imported script text file and stores it.	
	currentLineNumber = 0								# current line number within script.
	currentCharacter = 0								# current character within line.
	keyPressed = False									# keeps the line_reading functions running if this is False.
	beatStart = time.time()								
	beatTime = 0										# stores beat time for a particular line_reading function.
	lineCount = sum(1 for _ in scriptData)
	for rawLine in range(lineCount):
		line = ''
		lineLength = len(scriptData[currentLineNumber])
		lineData = scriptData[currentLineNumber]
		lineType = ''
		lineType += lineData[:3]
		line += lineData[3:]
		currentLineNumber += 1
		if (lineType == "[0]" or lineType == "[1]" or lineType == "[2]") and line[:3] != "	a:" and line[:3] != "	b:" and line[:3] != "	c:" and line[:3] != "	d:":
#			print "Current line number: " + str(currentLineNumber)
#			print "Line type: " + str(lineType)
#			print "Line: " + str(line)
#			print "Line length: " + str(lineLength)
			if lineType == "[0]":
				npc_line_reading(line)
			elif lineType == "[1]":
				player_line_reading(line)
			elif lineType == "[2]":
				npc_strange_line_reading(line)
		elif lineType == "---":
			print "END"
			break
	script.close()
	