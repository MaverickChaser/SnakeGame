import pygame
from pygame.locals import *

pygame.init()
#Colors 
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SILVER = (201, 192, 187)
BACKGROUND = (0, 0, 120)

RIGHT = (K_RIGHT, ord('d'))
DOWN = (K_DOWN, ord('s'))
UP = (K_UP, ord('w'))
LEFT = (K_LEFT, ord('a'))

#snake params

RADIUS = 10
DIAMETER = 2 * RADIUS
PRIZE_SIZE = DIAMETER

N = 4
MOVES = 8

START_X = 100

#score
SCORE_FIRST_X = 5
SCORE_FIRST_Y = 5

SCORE_SECOND_X = SCREEN_WIDTH - 120
SCORE_SECOND_Y = 5

#game states
PAUSE = 0
ON = 1
DURATION = 25000

#speed
dx, dy = DIAMETER, DIAMETER

#text
scoreFont = pygame.font.Font(None, 36)
timeFont = pygame.font.Font(None, 22)

directions = ((-1, 0), (0, -1), (1, 0), (0, 1))

def isOutside(cell):
	return cell[0] < RADIUS or cell[0] + RADIUS > SCREEN_WIDTH or cell[1] < RADIUS or cell[1] + RADIUS > SCREEN_HEIGHT

def getDist(c1, c2):
	return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])