import sys, time, random
from pygame.locals import *
from data.constants import *

# game loop to keep the game running.
def gameLoop():
	gameRunning = True
	while gameRunning == True:
		if pygame.event.get(pygame.QUIT):
			pygame.quit()
			sys.exit()
		pygame.display.update()

# heartTimer, general timing function for .
def heartTimer(stopValue, timerEvent):
	beatTime = 0
	heartStart = time.time()
	screen.blit(bgImage, (0, 0))
	stopValueTriggered = False
	responseChosen = ''
	while stopValueTriggered == False:
		for event in pygame.event.get():
			if event.type == stopValue:
				heartStop = time.time()
				beatTime += heartStop - heartStart
				print "IT WORKED."
				print "BEATTIME: " + str(beatTime)
				stopValueTriggered = True
				pygame.quit()
				sys.exit()
	if beatTime <= 1:
		responseChosen += "[R1]"
	elif 1 < beatTime <= 3:
		responseChosen += "[R2]"
	elif 3 < beatTime <= 5:
		responseChosen += "[R3]"
		timerEvent
	elif 5 < beatTime:
		responseChosen += "[R4]"

# function that displays text, handles interrupt of line and returns beatTime.
def npc_line_reading(text, name):
	line = ''
	currentCharacter = 0
	keyPressed = False
	heartStart = time.time()
	beatTime = 0
	lineLength = len(text)
	line += name + " : "
	text_surface = lineFont.render(line, True, black)
	text_rect = text_surface.get_rect()
	screen.blit(text_surface, text_rect)
	nameTextWaitTime = 250
	pygame.display.update()
	pygame.time.wait(nameTextWaitTime)
	for character in range(len(text)):
		if pygame.event.get(pygame.KEYDOWN):
			keyPressed = True
			line += "--"
			text_surface = lineFont.render(line, True, black)
			screen.blit(bgImage, (0, 0))
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
			text_surface = lineFont.render(line, True, black)
			characterCountSurface = lineFont.render(str(currentCharacter), True, red)
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
	text_surface = lineFont.render(line, True, black)
	screen.blit(text_surface, (100, 200))
	pygame.display.update()
	pygame.time.wait(250)
	for character in range(len(text)):
		screen.blit(bgImage, (0, 0))
		line += text[character]
		currentCharacter += 1
		text_surface = lineFont.render(line, True, black)
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
	text_surface = lineFont.render(line, True, black)
	screen.blit(text_surface, (100, 200))
	pygame.display.update()
	pygame.time.wait(250)
	for character in range(len(text)):
		if pygame.event.get(pygame.KEYDOWN):
			keyPressed = True
			line += "--"
			text_surface = lineFont.render(line, True, black)
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
			text_surface = lineFont.render(line, True, black)
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
	screen.blit(bgImage, (0, 0))
	pygame.display.update()
	print "SCRIPTBREAK FUNCTION RUN"
	while status == 1:
		if pygame.event.get(pygame.KEYDOWN):
			return 0

def scriptHandler(state, scriptFile):
	script = open(("data/states/" + state + "/" + scriptFile), 'r')
	scriptData = script.readlines()
	currentLineNumber = 0
	nextLineNumber = currentLineNumber + 1
	lineCount = sum(1 for _ in scriptData)
	responseData = ''
	responseLine = ''
	responseChosen = ''
	responseLines = ''
	breakReached = False
	responseRead = False
	print "Total Line Count: " + str(lineCount) + "\n"
	while breakReached == False:
		if nextLineNumber <= lineCount:
			for rawLine in range(lineCount):
				line = ''
				lineData = scriptData[currentLineNumber].strip()
				lineType = lineData[:3]
				nextLine = ''
				nextLineType = ''
				isResponse = False
				charName = str(lineData[3:].split(":")[0])
				if nextLineNumber < lineCount:
					nextLine += scriptData[nextLineNumber].strip()
					nextLineType += nextLine[:3]
				if lineType != "---":
					if len(lineData.split(":")[1]) > 0:
						isResponse = True
					if isResponse == False:
						line += lineData.split(":")[2]
					elif isResponse == True:
						if lineData.split(":")[1] == responseChosen and len(responseChosen) > 0 and responseRead == False:
							line += lineData.split(":")[2]
							responseChosen = ''
							responseRead = True
						if lineData.split(":")[1] == "[R4]":
							responseRead = False
					if len(line) > 0:
						if lineType == "[0]":
							beatTime = npc_line_reading(line, charName)
							if beatTime <= 1:
								responseChosen += "[R1]"
							elif 1 < beatTime <= 3:
								responseChosen += "[R2]"
							elif 3 < beatTime <= 5:
								responseChosen += "[R3]"
							elif 5 < beatTime:
								responseChosen += "[R4]"
						elif lineType == "[1]":
							beatTime = player_line_reading(line, charName)
						elif lineType == "[2]":
							beatTime = npc_strange_line_reading(line, charName)
							if beatTime <= 1:
								responseChosen += "[R1]"
							elif 1 < beatTime <= 3:
								responseChosen += "[R2]"
							elif 3 < beatTime <= 5:
								responseChosen += "[R3]"
							elif 5 < beatTime:
								responseChosen += "[R4]"
				elif lineType == "---":
					breakReached = True
					if scriptBreak(1) == 0:
						breakReached = False
				print "Current Line Number: " + str(currentLineNumber)
				print "Character Speaking: " + charName
				print "Line Type: " + lineType
				print "Next Line Type: " + nextLineType
				print "Response Chosen: " + responseChosen
				print "Line: " + line
				print "Beat Time: " + str(beatTime) + "\n"
				currentLineNumber += 1
				nextLineNumber += 1
		else:
			break