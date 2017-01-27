import pygame

pygame.init()
# constant variables & pygame initialization
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

display_width = 800
display_height = 500
font = pygame.font.Font("freesansbold.ttf", 10)
screen = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('OIL//WATER')

#small = pg.image.load("large.png")
#w, h = small.get_size()
#large = pg.Surface((w * 2, h))
#colors = [small.get_at((x, 0)) for x in range(0, w, 32)]
#for x, color in zip(range(0, w * 2, 64), colors):
#    surf = pg.Surface((64, h))
#    surf.fill(color)
#   large.blit(surf, (x, 0))
#pg.image.save(large, "yuge.png")