#!/usr/bin/env python

import sys, time
import cPickle
import pygame
from pygame.locals import *

from shape import *
from random import *

Name = 'PyTetris'
Author = 'Deng Chunhui'
Email = 'chunchengfh@gmail.com'
Version = '0.2'
Date = '2008-03-13'

SHAPES = (BAR, BLOCK, TOE, SHAPE_S, SHAPE_Z, SHAPE_F, SHAPE_7)
X_MAX = 10
Y_MAX = 20
INIT_SPEED = 40  # init block drop speed
drop_speed = INIT_SPEED
clock2 = pygame.time.Clock()

###########################
from colors import *

GRID_SIZE = 20
def draw_box(screen, x, y, c):
        lighter = calc_flash(c, 30)
        darker = calc_brightness(c, 0.7)
        pygame.draw.rect(screen, lighter, (x, y, GRID_SIZE-2,GRID_SIZE-2), 0)
        drawx = x + GRID_SIZE-2
        drawy = y + GRID_SIZE-2
        pygame.draw.polygon(screen, darker, ((x,drawy),(drawx,y),(drawx,drawy)), 0)
        pygame.draw.rect(screen, c, (x+3, y+3, GRID_SIZE-7, GRID_SIZE-7),0)


def move_left(block, grid):
	if block.type == 0:  # BAR
		if block.direction == 0 or block.direction == 2:
			if block.blockx+1 <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+3][block.blockx] == 8):
					return 1
			else:	return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blockx <= 0: return 0
			elif grid.grid[block.blocky][block.blockx-1] == 8:
				return 1
			else:
				return 0
	elif block.type == 1:  # BLOCK
		if block.blockx+1 <= 0:
			return 0
		elif (grid.grid[block.blocky+1][block.blockx] == 8 and
			grid.grid[block.blocky+2][block.blockx] == 8):
				return 1
		else:
			return 0
	elif block.type == 2:  # TOE
		if block.direction == 0:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx-1] == 8):
					return 1
			else:	return 0
		elif block.direction == 1:
			if block.blockx+1 <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
				return 1
			else:
				return 0
		elif block.direction == 2:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx-1] == 8):
					return 1
			else:	return 0
		elif block.direction == 3:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx-1] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
					return 1
			else:	return 0
	elif block.type == 3:  # SHAPE_S
		if block.direction == 0 or block.direction == 2:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx-1] == 8):
					return 1
			else:	return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blockx+1 <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8):
				return 1
			else:
				return 0
	elif block.type == 4:  # SHAPE_Z
		if block.direction == 0 or block.direction == 2:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky+1][block.blockx-1] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
					return 1
			else:	return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blockx+1 <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
				return 1
			else:
				return 0
	elif block.type == 5:  # SHAPE_F
		if block.direction == 0:
			if block.blockx+1 <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
					return 1
			else:	return 0
		elif block.direction == 1:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky+1][block.blockx-1] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8):
				return 1
			else:
				return 0
		if block.direction == 2:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx-1] == 8):
					return 1
			else:	return 0
		elif block.direction == 3:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx-1] == 8 and
				grid.grid[block.blocky+1][block.blockx-1] == 8):
				return 1
			else:
				return 0
	elif block.type == 6:  # SHAPE_7
		if block.direction == 0:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx-1] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
					return 1
			else:	return 0
		elif block.direction == 1:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+1][block.blockx-1] == 8):
				return 1
			else:
				return 0
		if block.direction == 2:
			if block.blockx+1 <= 0: return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
					return 1
			else:	return 0
		elif block.direction == 3:
			if block.blockx <= 0: return 0
			elif (grid.grid[block.blocky+1][block.blockx-1] == 8 and
				grid.grid[block.blocky+2][block.blockx-1] == 8):
				return 1
			else:
				return 0

def move_right(block, grid):
	if block.type == 0:  # BAR
		if block.direction == 0 or block.direction ==2:
			if block.blockx+2 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8 and
				grid.grid[block.blocky+3][block.blockx+2] == 8):
				return 1
			else:
				return 0
		elif block.direction == 1 or block.direction ==3:
			if block.blockx+4 >= 10: return 0
			elif grid.grid[block.blocky][block.blockx+4] == 8:
				return 1
			else:
				return 0
	elif block.type == 1:  # BLOCK
		if block.blockx+3 >= 10:
			return 0
		elif (grid.grid[block.blocky+1][block.blockx+3] == 8 and
			grid.grid[block.blocky+2][block.blockx+3] == 8):
				return 1
		else:
			return 0
	elif block.type == 2:  # TOE
		if block.direction == 0:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8):
					return 1
			else:	return 0
		elif block.direction == 1:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else:
				return 0
		elif block.direction == 2:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky+2][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8):
					return 1
			else:	return 0
		elif block.direction == 3:
			if block.blockx+2 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else:	return 0
	elif block.type == 3:  # SHAPE_S
		if block.direction == 0 or block.direction == 2:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky+1][block.blockx+3] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else:	return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8 and
				grid.grid[block.blocky+2][block.blockx+3] == 8):
				return 1
			else:
				return 0
	elif block.type == 4:  # SHAPE_Z
		if block.direction == 0 or block.direction == 2:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+3] == 8):
					return 1
			else:	return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+3] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				return 0
	elif block.type == 5:  # SHAPE_F
		if block.direction == 0:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+3] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else:	return 0
		elif block.direction == 1:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky+1][block.blockx+3] == 8 and
				grid.grid[block.blocky+2][block.blockx+3] == 8):
				return 1
			else:
				return 0
		if block.direction == 2:
			if block.blockx+2 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else:	return 0
		elif block.direction == 3:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8):
				return 1
			else:
				return 0
	elif block.type == 6:  # SHAPE_7
		if block.direction == 0:
			if block.blockx+2 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else:	return 0
		elif block.direction == 1:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+3] == 8 and
				grid.grid[block.blocky+1][block.blockx+3] == 8):
				return 1
			else:
				return 0
		if block.direction == 2:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+3] == 8):
					return 1
			else:	return 0
		elif block.direction == 3:
			if block.blockx+3 >= 10: return 0
			elif (grid.grid[block.blocky+1][block.blockx+3] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8):
				return 1
			else:
				return 0
		return 1

def move_down(block, grid):
	if block.type == 0:  # BAR
		if block.direction == 0 or block.direction == 2:
			if block.blocky+4 >= 20 or grid.grid[block.blocky+4][block.blockx+1] != 8:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+3][block.blockx+1] = block.type
				return 0
			else:
				return 1
		elif block.direction == 1 or block.direction == 3:
			if block.blocky+2 >= 20:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx+3] = block.type
				return 0
			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+3] == 8):
				return 1
			else:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx+3] = block.type
				return 0
	elif block.type == 1:  # BLOCK
		if block.blocky+3 >= 20:
			grid.grid[block.blocky+1][block.blockx+1] = block.type
			grid.grid[block.blocky+1][block.blockx+2] = block.type
			grid.grid[block.blocky+2][block.blockx+1] = block.type
			grid.grid[block.blocky+2][block.blockx+2] = block.type
			return 0
		elif (grid.grid[block.blocky+3][block.blockx+1] == 8 and
			grid.grid[block.blocky+3][block.blockx+2] == 8):
				return 1
		else:
			grid.grid[block.blocky+1][block.blockx+1] = block.type
			grid.grid[block.blocky+1][block.blockx+2] = block.type
			grid.grid[block.blocky+2][block.blockx+1] = block.type
			grid.grid[block.blocky+2][block.blockx+2] = block.type
			return 0

	elif block.type == 2:  # TOE
		if block.direction == 0:
			if block.blocky+2 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0

		elif block.direction == 1:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0
		elif block.direction == 2:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0
		elif block.direction == 3:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				return 0
	elif block.type == 3:  # SHAPE_S
		if block.direction == 0 or block.direction == 2:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx] == 8 and
				grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+3][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0
	elif block.type == 4:  # SHAPE_Z
		if block.direction == 0 or block.direction == 2:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+3][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0
	elif block.type == 5:  # SHAPE_F
		if block.direction == 0:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0

		elif block.direction == 1:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+3][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0
		elif block.direction == 2:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx] == 8 and
				grid.grid[block.blocky+3][block.blockx+1] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx] = block.type
				return 0
		elif block.direction == 3:
			if block.blocky+2 >= 20:
				grid.grid[block.blocky][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0
	elif block.type == 6:  # SHAPE_7
		if block.direction == 0:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx] = block.type
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0

			elif (grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+3][block.blockx+1] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx] = block.type
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				return 0

		elif block.direction == 1:
			if block.blocky+2 >= 20:
				grid.grid[block.blocky][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+2] = block.type
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				return 0
		elif block.direction == 2:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx+1] == 8 and
				grid.grid[block.blocky+3][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+1] = block.type
				grid.grid[block.blocky+2][block.blockx+2] = block.type
				return 0
		elif block.direction == 3:
			if block.blocky+3 >= 20:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx] = block.type
				return 0

			elif (grid.grid[block.blocky+3][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else:
				grid.grid[block.blocky+1][block.blockx] = block.type
				grid.grid[block.blocky+1][block.blockx+1] = block.type
				grid.grid[block.blocky+1][block.blockx+2] = block.type
				grid.grid[block.blocky+2][block.blockx] = block.type
				return 0


def change_direction(block, grid):
	if block.type == 0:  # BAR
		if block.direction == 0 or block.direction == 2:
			if block.blockx+1 < 1 or block.blockx+4 > 10:
				return 0
		if block.direction == 1 or block.direction == 3:
			if block.blocky+2 > 20:
				return 0
		if (grid.grid[block.blocky][block.blockx] == 8 and
			grid.grid[block.blocky+2][block.blockx+2] == 8 and
			grid.grid[block.blocky+2][block.blockx+3] == 8 and
			grid.grid[block.blocky+3][block.blockx+2] == 8 and
			grid.grid[block.blocky+3][block.blockx+3] == 8):
			if block.direction == 0 or block.direction == 2:
				if (grid.grid[block.blocky+1][block.blockx] == 8 and
					grid.grid[block.blocky+1][block.blockx+2] == 8 and
					grid.grid[block.blocky+1][block.blockx+3] == 8):
					return 1
			elif block.direction == 1 or block.direction == 3:
				if (grid.grid[block.blocky][block.blockx+1] == 8 and
					grid.grid[block.blocky+2][block.blockx+1] == 8 and
					grid.grid[block.blocky+3][block.blockx+1] == 8):
					return 1
			else:
				return 0
		else: return 0
	elif block.type == 1:  # BLOCK
		return 1
	elif block.type == 2:  # TOE
		if block.direction == 0:
			if block.blocky+2 >= 20:
				return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8):
					return 1
			else: return 0
		elif block.direction == 1:
			if block.blockx+1 < 1:
				return 0
			elif (grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
					return 1
			else: return 0
		elif block.direction == 2:
			if (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
					return 1
			else: return 0
		elif block.direction == 3:
			if block.blockx+2 >= 20:
				return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8):
					return 1
			else: return 0
	elif block.type == 3:  # SHAPE_S
		if block.direction == 0 or block.direction == 2:
			if (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else: return 0
		elif block.direction == 1 or block.direction == 3:
			if block.blockx+1 < 1:
				return 0
			elif (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8):
				return 1
			else: return 0
	elif block.type == 4:  # SHAPE_Z
		if block.direction == 0 or block.direction == 2:
			if (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8):
				return 1
		elif block.direction == 1 or block.direction == 3:
			if block.blockx+1 < 1:
				return 0
			elif (grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
		else: return 0
	elif block.type == 5:  # SHAPE_F
		if block.direction == 0:
			if block.blockx+1 < 1:
				return 0
			elif (grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else: return 0
		elif block.direction == 1:
			if (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8):
				return 1
			else: return 0
		elif block.direction == 2:
			if block.blockx+2 >= 10:
				return 0
			elif (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8):
				return 1
			else: return 0
		elif block.direction == 3:
			if block.blocky+2 >= 20:
				return 0
			if (grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else: return 0
	elif block.type == 6:  # SHAPE_7
		if block.direction == 0:
			if block.blockx+2 >= 10:
				return 0
			if (grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8):
				return 1
			else: return 0
		elif block.direction == 1:
			if block.blocky+2 >= 20:
				return 0
			if (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else: return 0
		elif block.direction == 2:
			if block.blockx+1 < 1:
				return 0
			if (grid.grid[block.blocky+1][block.blockx] == 8 and
				grid.grid[block.blocky+2][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+2] == 8 and
				grid.grid[block.blocky+1][block.blockx+2] == 8):
				return 1
			else: return 0
		elif block.direction == 3:
			if (grid.grid[block.blocky][block.blockx] == 8 and
				grid.grid[block.blocky][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+1] == 8 and
				grid.grid[block.blocky+2][block.blockx+2] == 8):
				return 1
			else: return 0


class Count:
	'''count the score'''
	def __init__(self, count):
		self.count = count
		self.line = 0

	def update_score(self, line, screen):
		global drop_speed
		if line == 0.1:
			self.count += 10
		else:
			self.line += line
			if line == 1:
				self.count += 100
			elif line == 2:
				self.count += 300
			elif line == 3:
				self.count += 600
			elif line == 4:
				self.count += 1000

		if drop_speed <= 6:
			drop_speed = 6
		else:
			drop_speed = INIT_SPEED - (self.line / 8)
		self.draw_count(screen)


	def draw_highscore(self, screen):
		myfont = pygame.font.SysFont("arial", 24)
#		myfont.set_bold(1)
		try:
			file = open('highscore.dat', 'rb')
			self.highscore = str(cPickle.load(file))
		except:
			self.highscore = '0'
		highfont_surface = myfont.render("High Score", True, (0, 128, 64)) #, (255, 255, 0))
		highscore_surface = myfont.render(self.highscore, True, (0, 255, 64)) #, (255, 255, 0))
		highfont_pos = highfont_surface.get_rect()
		highscore_pos = highscore_surface.get_rect()

		highfont_pos.topright = (135, 20)
		highscore_pos.topright = (135, 50)
		screen.blit(highfont_surface, highfont_pos)
		screen.blit(highscore_surface, highscore_pos)


	def draw_author(self, screen):
		myfont = pygame.font.SysFont("arial", 20)
#		author_surface = myfont.render("By: Deng Chunhui", True, (0, 128, 64)) #, (255, 255, 0))
		email_surface = myfont.render("chunchengfh", True, (0, 0, 64)) #, (255, 255, 0))
		date_surface = myfont.render("( 2008 - 03 )", True, (0, 0, 64)) #, (255, 255, 0))
#		author_pos = author_surface.get_rect()
		email_pos = email_surface.get_rect()
		date_pos = date_surface.get_rect()

#		author_pos.topleft = (2, 340)
		email_pos.topleft = (20, 360)
		date_pos.topleft = (30, 380)

#		screen.blit(author_surface, author_pos)
		screen.blit(email_surface, email_pos)
		screen.blit(date_surface, date_pos)


	def draw_count(self, screen):
		myfont = pygame.font.SysFont("arial", 24)
#		myfont.set_bold(1)
		scorefont_surface = myfont.render("Score", True, (0, 128, 64)) #, (255, 255, 0))
		linefont_surface = myfont.render("Line", True, (0, 128, 64)) #, (255, 255, 0))
		nextblock_surface = myfont.render("Next block", True, (0, 128, 64)) #, (255, 255, 0))
		scorefont_pos = scorefont_surface.get_rect()
		linefont_pos = linefont_surface.get_rect()
		nextblock_pos = nextblock_surface.get_rect()
		scorefont_pos.topright = (120, 20)
		linefont_pos.topright = (120, 120)
		nextblock_pos.topright = (130, 250)

		count_surface = myfont.render(str(self.count), True, (0, 255, 64)) #, (255, 255, 0))
		line_surface = myfont.render(str(self.line), True, (0, 255, 64)) #, (255, 255, 0))
		count_pos = count_surface.get_rect()
		line_pos = line_surface.get_rect()
		count_pos.topright = (120, 50)
		line_pos.topright = (120, 150)

		screen.fill((128, 128, 128))
		screen.blit(scorefont_surface, scorefont_pos)
		screen.blit(linefont_surface, linefont_pos)
		screen.blit(nextblock_surface, nextblock_pos)
		screen.blit(count_surface, count_pos)
		screen.blit(line_surface, line_pos)

	
	def save_highscore(self):
		if self.count > int(self.highscore):
			try:
				file = open('highscore.dat', 'wb')
				cPickle.dump(self.count, file, 1)
			except:
				print 'Why?'
				pass


class Block:
	'''seven types of block, 4*4'''
	def __init__(self, type, direction):
		self.type = type # type is acciationed with color
		self.direction = direction # 0: _|_
		self.blockx = 3
		self.blocky = 0
		self.block = SHAPES[self.type] # [self.direction]

	def draw_block(self, screen, x, y):
		for i in range(0, 4):
			for j in range(0, 4):
				if self.block[self.direction][j][i] == 1 :
#					pygame.draw.rect(screen, COLOR[self.type], Rect(x+i*20, y+j*20, 20, 20))
					draw_box(screen, x+i*20, y+j*20, COLOR[self.type])


class Grid:
	'''include all pieces of dropped blocks, 10*20'''
	def __init__(self):
		self.grid = [	[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
				[8, 8, 8, 8, 8, 8, 8, 8, 8, 8]]


	def draw_grid(self, screen):
		for i in range(0, 20):
			for j in range(0, 10):
				if self.grid[i][j] < 8:
					color_index = self.grid[i][j]
#					pygame.draw.rect(screen, COLOR[color_index], Rect(j*20, i*20, 20, 20))
					draw_box(screen, j*20, i*20, COLOR[color_index])


	def check_tetris(self):
		count = 0
		for row in range(0, Y_MAX):
			if 8 not in self.grid[row]:
				count += 1
				self.update(row)
				for _ in range(0, 2): # pause for a little time
					clock2.tick(8)

		return count


	def update(self, row):
		for i in range(0, row):
			self.grid[row-i] = self.grid[row-i-1]
			self.grid[0] =[8, 8, 8, 8, 8, 8, 8, 8, 8, 8]


class Game:
	def __init__(self):
		pygame.init()
		pygame.key.set_repeat(70)

		self.topscreen = pygame.display.set_mode((480,400), 0, 32)
		self.leftscreen = self.topscreen.subsurface((0,0), (140, 280))
		self.nextblockscreen = self.topscreen.subsurface((20,280), (100, 100))
		self.rightscreen = self.topscreen.subsurface((340,0), (140, 400))
		self.screen = self.topscreen.subsurface((140,0), (200, 400))
		pygame.display.set_caption("PyTetris (version: " + Version + ")")
		self.topscreen.fill((128, 128, 128))

		self.grid = Grid()
		self.block = Block(randint(0,6), 0)
		self.nextblock = randint(0,6)
		self.draw_nextblock(self.nextblock, self.nextblockscreen)
		self.count = Count(0)
		self.score = 0
		self.clock = pygame.time.Clock()

		self.count.draw_highscore(self.rightscreen)
		self.count.draw_author(self.rightscreen)
		self.count.draw_count(self.leftscreen)
		self.ready()


	def ready(self):
#		if click_button == 1:
			self.begin_game()


	def draw_nextblock(self, type, screen):
		screen.fill((0,0,0))
		block = SHAPES[type] # [self.direction]
		for i in range(0, 4):
			for j in range(0, 4):
				if block[0][j][i] == 1 :
					draw_box(screen, 10+i*20, 10+j*20, COLOR[type])


	def game_over(self, screen):
		self.count.save_highscore()

		myfont = pygame.font.SysFont("arial", 38)
#		myfont.set_bold(1)
#		gameover_surface = myfont.render(" Game Over! ", True, (0, 128, 64), (132, 196, 60))
		gameover_surface = myfont.render(" Game Over! ", True, (0, 128, 64), (128, 128, 128))
		gameover_pos = gameover_surface.get_rect()
		gameover_pos.topleft = (15, 170)

#		self.block.draw_block(self.screen, self.block.blockx*20, self.block.blocky*20)
		self.grid.draw_grid(self.screen)
		screen.blit(gameover_surface, gameover_pos)
		pygame.display.update()

		while True:
			time.sleep(0.1)
			for event in pygame.event.get():
				if event.type == QUIT:
					sys.exit()


	def check_game_over(self):
		for i in range(0, 4):
			for j in range(0, 4):
				if(self.block.block[self.block.direction][i][j] != 0 and
					self.grid.grid[j][i+3] != 8):
						return 1

		return 0


	def check_event(self):
		move_x = move_y = 0
		for event in pygame.event.get():
			if event.type == QUIT:
				sys.exit()

			if event.type == KEYDOWN:
				if event.key == K_p or event.key == K_SPACE:
				    while True:
					time.sleep(0.1)
					for event in pygame.event.get():
						if event.type == QUIT:
							sys.exit()
						if event.type == KEYDOWN:
							if event.key == K_p or event.key == K_SPACE:
								return

				if event.key == K_LEFT:
					move_x = -1 * move_left(self.block, self.grid)
				elif event.key == K_RIGHT:
					move_x = +1 * move_right(self.block, self.grid)
				elif event.key == K_DOWN:
					moviable = move_down(self.block, self.grid)
					if moviable == 1:
						move_y = +1 * 1
					else:
						self.count.update_score(0.1, self.leftscreen)
						self.block = Block(self.nextblock, 0)
						self.nextblock = randint(0,6)
						self.draw_nextblock(self.nextblock, self.nextblockscreen)

						if self.check_game_over() == 1:
							self.game_over(self.screen)

				elif event.key == K_UP:
					if change_direction(self.block, self.grid):
						self.block.direction = (self.block.direction+1)%4

			elif event.type == KEYUP:
				if event.key == K_LEFT:
					move_x = 0
				elif event.key == K_RIGHT:
					move_x = 0
				elif event.key == K_DOWN:
					move_y = 0
				elif event.key == K_UP:
					move_y = 0

			self.block.blockx += move_x
			self.block.blocky += move_y


	def begin_game(self):
#		print 'Begin Game...'

		drop_interval = 0
		while True:
			self.clock.tick(60)
			drop_interval = drop_interval+1
			self.screen.fill((0,0,0))

			self.check_event()
			if drop_interval % (drop_speed) == 0:
				drop_interval = 0
				moviable = move_down(self.block, self.grid)
				if moviable == 1:
					move_y = +1 * 1
					self.block.blocky += move_y
				else:
					self.count.update_score(0.1, self.leftscreen)
					self.block = Block(self.nextblock, 0)
					self.nextblock = randint(0,6)
					self.draw_nextblock(self.nextblock, self.nextblockscreen)

					if self.check_game_over() == 1:
						self.game_over(self.screen)

			score = self.grid.check_tetris()
			if score > 0:
				self.count.update_score(score, self.leftscreen)
			self.block.draw_block(self.screen, self.block.blockx*20, self.block.blocky*20)
			self.grid.draw_grid(self.screen)

			pygame.display.update()


def main():
	game = Game()


if __name__ == '__main__':
	main()
