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

# game loop to keep the game running.
def gameLoop():
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			pygame.quit()
			sys.exit()
		pygame.display.update()

# function that displays text, handles interrupt of line and returns beatTime.
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
			pygame.time.wait(50)
			screen.blit(bgImage, (0, 0))
			pygame.display.update()
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
			keyPressed = True
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
			keyPressed = True
	return beatTime

def scriptBreak(status):
	while status == 1:
		if pygame.event.get(pygame.KEYDOWN):
			return 0
	
def scriptHandler(scriptFile):
	script = open(scriptFile, 'r')
	scriptData = script.readlines()
	currentLineNumber = 0
	nextLineNumber = currentLineNumber + 1
	lineCount = sum(1 for _ in scriptData)
	responseLines = ''
	response = ''
	playerResponded = False
	breakReached = False
	print "Total line count: " + str(lineCount) + "\n"
	while breakReached == False:
		for rawLine in range(lineCount):
			line = ''
			lineLength = len(scriptData[currentLineNumber])
			lineData = scriptData[currentLineNumber].strip()
			lineType = lineData[:3]
			nextLine = ''
			charName = str(lineData[3:].split(":")[0])
			nextLineIsResponse = False
			nextLineCharName = ''
			nextLineType = ''
			if (currentLineNumber + 1) < lineCount:
				nextLine += scriptData[currentLineNumber + 1].strip()
				if nextLine != "---":
					if len(nextLine[3:].split(":")[1]) > 0 and len(responseLines) == 0:
						responseLines += nextLine + "\n"
						responseLines += scriptData[nextLineNumber + 1].strip() + "\n"
						responseLines += scriptData[nextLineNumber + 2].strip() + "\n"
						responseLines += scriptData[nextLineNumber + 3].strip() + "\n"
						nextLineIsResponse = True
			if lineType != "---" and playerResponded == False:
				line += lineData.split(":")[2]
				responseChosen = ''
				isResponseChecker = len(lineData[3:].split(":")[1])
				isResponse = False
				if isResponseChecker > 0:
					isResponse = True
				if lineType == "[0]" and isResponse == False:
					beatTime = npc_line_reading(line, charName)
					if beatTime <= 1 and nextLineIsResponse == True:
						responseChosen += "[R1]"
						playerResponded = True
					elif 1 < beatTime <= 3 and nextLineIsResponse == True:
						responseChosen += "[R2]"
						playerResponded = True
					elif 3 < beatTime <= 5 and nextLineIsResponse == True:
						responseChosen += "[R3]"
						playerResponded = True
					elif 5 < beatTime and nextLineIsResponse == True:
						responseChosen += "[R4]"
						playerResponded = True
				elif lineType == "[1]" and isResponse == False:
					beatTime = player_line_reading(line, charName)
				elif lineType == "[2]" and isResponse == False:
					beatTime = npc_strange_line_reading(line, charName)
					if beatTime <= 1 and nextLineIsResponse == True and playerResponded == False:
						responseChosen += "[R1]"
						playerResponded = True
					elif 1 < beatTime <= 3 and nextLineIsResponse == True and playerResponded == False:
						responseChosen += "[R2]"
						playerResponded = True
					elif 3 < beatTime <= 5 and nextLineIsResponse == True and playerResponded == False:
						responseChosen += "[R3]"
						playerResponded = True
					elif 5 < beatTime and nextLineIsResponse == True and playerResponded == False:
						responseChosen += "[R4]"
						playerResponded = True
				if responseChosen == "[R1]":
					responseData = responseLines.split("\n")[0]
					response = responseData.split(":")[2]
					responseName = responseData[3:].split(":")[0]
					responseLineType = responseData[:3]
				elif responseChosen == "[R2]":
					responseData = responseLines.split("\n")[1]
					response = responseData.split(":")[2]
					responseName = responseData[3:].split(":")[0]
					responseLineType = responseData[:3]
				elif responseChosen == "[R3]":
					responseData = responseLines.split("\n")[2]
					response = responseData.split(":")[2]
					responseName = responseData[3:].split(":")[0]
					responseLineType = responseData[:3]
				elif responseChosen == "[R4]":
					responseData = responseLines.split("\n")[3]
					response = responseData.split(":")[2]
					responseName = str(responseData[3:].split(":")[0])
					responseLineType = responseData[:3]
			elif playerResponded == True:
				if responseLineType == "[0]":
					npc_line_reading(response, responseName)
					playerResponded = False
				if responseLineType == "[1]":
					player_line_reading(response, responseName)
					playerResponded = False
				if responseLineType ==  "[2]":
					npc_strange_line_reading(response, responseName)
					playerResponded = False
			elif line == "---":
				breakReached = True
				while breakReached == True:
					screen.blit(bgImage, (0, 0))
					scriptBreak(1)
					if scriptBreak(1) == 0:
					breakReached = False
			currentLineNumber += 1
			nextLineNumber += 1
			print "CHARACTER SPEAKING: " + charName
			print "CURRENT LINE NUMBER: " + str(currentLineNumber)
			print "LINE TYPE: " + lineType
			print "LINE: " + line
			print "BEATTIME: " + str(beatTime)
			print "NEXT LINE IS RESPONSE: " + str(nextLineIsResponse)
			print "RESPONSE CHOSEN: " + responseChosen
			print "RESPONSE LINE: " + response
			print "NEXT LINE: " + nextLine + "\n"
		
		