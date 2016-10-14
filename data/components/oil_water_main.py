import pygame, sys, time, random
from pygame.locals import *

# constant variables & pygame initialization
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

pygame.init()
display_width = 800
display_height = 500
text_bg_width = 600
text_bg_height = 200
font = pygame.font.Font("freesansbold.ttf", 10)
screen = pygame.display.set_mode((display_width, display_height))
text_bg = pygame.Surface((text_bg_width, text_bg_height))
text_bg = text_bg.convert_alpha()
bgImage = pygame.image.load("spacetrees.png")
pygame.display.set_caption('OIL//WATER')


gameRunning = True

# game loop to keep game open and running
def gameLoop():
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			pygame.quit()
			sys.exit()
		pygame.display.update()
	
# function that displays text, handles interrupt of line and measures 
def npc_line_reading(text, name):
	line = ''
	currentCharacter = 0
	keyPressed = False
	heartStart = time.time()
	beatTime = 0
	lineLength = len(text)
	line += name + " : "
	text_surface = font.render(line, True, black)
	text_rect = text_surface.get_rect()
	screen.blit(text_surface, text_rect)
	nameTextWaitTime = 250
	pygame.display.update()
	pygame.time.wait(nameTextWaitTime)
	for character in range(len(text)):
		if pygame.event.get(pygame.KEYDOWN):
			keyPressed = True
			line += "--"
			text_surface = font.render(line, True, black)
			screen.blit(text_surface, text_rect)
			pygame.display.update()
			print "Line interrupted!"
			pygame.time.wait(50)
			screen.blit(bgImage, (0, 0))
			pygame.display.update()
			print beatTime
			break
		elif keyPressed == False:
			screen.blit(bgImage, (0, 0))
			line += text[character]
			currentCharacter += 1
			text_surface = font.render(line, True, black)
			characterCountSurface = font.render(str(currentCharacter), True, red)
			text_rect = text_surface.get_rect()
			screen.blit(text_surface, text_rect)
			screen.blit(characterCountSurface, (100, 100))
			if currentCharacter == (lineLength - 10):
				heartStart = time.time()
				print "Heart Timer auto-started!"
			pygame.display.update()
			pygame.time.wait(50)
	while keyPressed == False:
		if pygame.event.get(pygame.KEYDOWN):
			heartStop = time.time()
			beatTime = heartStop - heartStart
			screen.blit(bgImage, (0, 0))
			pygame.display.update()
			print "Heart Timer stopped!"
			print beatTime
			keyPressed = True
	print "TESTING BEATTIME: " + str(beatTime)
	return beatTime

def player_line_reading(text, name):
	line = ''
	keyPressed = False
	lineLength = len(text)
	currentCharacter = 0
	line += name + " : "
	text_surface = font.render(line, True, black)
	screen.blit(text_surface, (100, 200))
	pygame.display.update()
	pygame.time.wait(250)
	for character in range(len(text)):
		screen.blit(bgImage, (0, 0))
		line += text[character]
		currentCharacter += 1
		text_surface = font.render(line, True, black)
		screen.blit(text_surface, (100, 200))
		pygame.display.update()
		pygame.time.wait(50)
		if currentCharacter == lineLength:
			print "End of the line!"
	while keyPressed == False:
		if pygame.event.get(pygame.KEYDOWN):
			screen.blit(bgImage, (0, 0))
			pygame.display.update()
			keyPressed = True
			break

def npc_strange_line_reading(text, name):
	line = ''
	lineLength = len(text)
	currentCharacter = 0
	keyPressed = False
	heartStart = time.time()
	beatTime = 0
	line += name + " : "
	text_surface = font.render(line, True, black)
	screen.blit(text_surface, (100, 200))
	pygame.display.update()
	pygame.time.wait(250)
	for character in range(len(text)):
		if pygame.event.get(pygame.KEYDOWN):
			keyPressed = True
			line += "--"
			text_surface = font.render(line, True, black)
			screen.blit(text_surface, (100, 200))
			pygame.display.update()
			pygame.time.wait(50)
			screen.blit(bgImage, (0, 0))
			pygame.display.update()
			print "Line interrupted!"
			print beatTime
			break
		elif keyPressed == False:
			screen.blit(bgImage, (0, 0))
			random_char_index = random.randint(0,lineLength - 1)
			line += '%s' % text[random_char_index]
			currentCharacter += 1
			text_surface = font.render(line, True, black)
			screen.blit(text_surface, (100, 200))
			pygame.display.update()
			pygame.time.wait(50)
			if currentCharacter == lineLength - 10:
				heartStart = time.time()
				print "Heart Timer auto-started!"
	while keyPressed == False:
		if pygame.event.get(pygame.KEYDOWN):
			heartStop = time.time()
			beatTime = heartStop - heartStart
			screen.blit(bgImage, (0, 0))
			pygame.display.update()
			print "Heart Timer stopped!"
			print beatTime
			keyPressed = True
	return beatTime

def scriptHandler(scriptFile):
	script = open(scriptFile, 'r')						# imports script text file.
	scriptData = script.readlines()						# reads the imported script text file and stores it.	
	currentLineNumber = 0								# current line number within script.
	lineCount = sum(1 for _ in scriptData)
	responseLines = ''
	for rawLine in range(lineCount):
		line = ''
		lineLength = len(scriptData[currentLineNumber])
		lineData = scriptData[currentLineNumber].strip()
		lineType = ''
		lineType += lineData[:3]
		currentLineNumber += 1
		if (lineType == "[0]" or lineType == "[1]" or lineType == "[2]"):
			charName = str(lineData[3:].split(":")[0])
			charNameLength = len(charName)
			isResponseChecker = len(lineData[3:].split(":")[1])
			isResponse = False
			nextLineIsResponse = False
			playerResponded = False
			if (currentLineNumber + 1) < lineCount:
				nextLine = scriptData[currentLineNumber + 1].strip()
				if nextLine != "---":
					nextLineResponseChecker = len(nextLine[3:].split(":")[1])
					print "Length of next line response checker: " + str(nextLineResponseChecker)
			if nextLineResponseChecker > 0:
				print "Next line is a response!"
				nextLineIsResponse = True
				responseLines += nextline + "\n"
			if isResponseChecker > 0:
				isResponse = True
				line += lineData[(10 + charNameLength):]
				print "isResponse: " + str(isResponse)
				print "Response Lines:\n" + responseLines
				print "Testing line isolation: " + responseLines.split("\n")[currentLineNumber]
			else:
				line += lineData[(5 + charNameLength):]
				nextLineIsResponse = False
				responseLines = ''
			print "CHARACTER SPEAKING: " + charName
			print "CHARACTER NAME LENGTH: " + str(charNameLength)
			print "Current line number: " + str(currentLineNumber)
			print "Line type: " + str(lineType)
			print "Line: " + str(line)
			print "Line length: " + str(lineLength)
			if lineType == "[0]":
				beatTime = npc_line_reading(line, charName)
				if beatTime <= 1 and nextLineIsResponse == True:
					print responseLines[0]
				elif 1 < beatTime <= 3 and nextLineIsResponse == True:
					print responseLines[1]
				elif 3 < beatTime <= 5 and nextLineIsResponse == True:
					print responseLines[2]
				elif nextLineIsResponse == True:
					print responseLines[3]
			elif lineType == "[1]":
				player_line_reading(line, charName)
			elif lineType == "[2]":
				beatTime = npc_strange_line_reading(line, charName)
				if beatTime <= 1:
					print "You're too hasty!"
				elif 1 < beatTime <= 3:
					print "You kind of thought about it."
				elif 3 < beatTime <= 5:
					print "You're a thinker!"
				else:
					print "You're a slow-poke."
		elif lineType == "---":
			print "END"
			break
	script.close()