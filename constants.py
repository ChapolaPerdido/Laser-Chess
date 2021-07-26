import pygame

# Window constants ------------------------------------------#
RESOLUTION = (32, 32)

WIDTH, HEIGHT = 700, 700
ROWS, COLUMNS = 10, 10

# Board constants ------------------------------------------#

board_image = pygame.image.load('sprites/board.png')
BOARD_X0 = 50
BOARD_Y0 = 50

board = pygame.transform.scale(board_image, (600, 600))

PURPLE = (255, 0, 255, 0)
GRID_ALPHA = 0

