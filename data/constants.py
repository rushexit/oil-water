import pygame
from pygame.locals import *
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

display_width = 800
display_height = 400
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('OIL//WATER')
bgImage = pygame.image.load("spacetrees.png")

lineFont = pygame.font.Font("freesansbold.ttf", 10)
menuLabelFont = pygame.font.Font("freesansbold.ttf", 14)
introFont = pygame.font.Font("freesansbold.ttf", 20)