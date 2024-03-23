import pygame

pygame.init()

WIDTH = 900
HEIGHT = 900
BOTMARGIN = 100

FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT + BOTMARGIN))
clock = pygame.time.Clock()
font = pygame.font.Font("font/LEMONMILK-Regular.otf",BOTMARGIN // 2)
