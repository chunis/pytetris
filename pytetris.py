#!/usr/bin/env python

import sys, time
import pygame
from pygame.locals import *

from shape import *
from random import *

Name = 'PyTetris'
Author = 'Deng Chunhui'
Email = 'chunchengfh@gmail.com'
Version = '0.0.2-dev'
Date = '2008-02-18'

SHAPES = (BAR, BLOCK, TOE, SHAPE_S, SHAPE_Z, SHAPE_F, SHAPE_7)
X_MAX = 10
Y_MAX = 20
INIT_SPEED = 15  # init block drop speed
clock2 = pygame.time.Clock()


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
			if block.blocky+2 > 20:
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
			if block.blockx+2 > 20:
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

	def update_score(self, line, speed):
		if line == 1:
			self.count += 100
		elif line == 2:
			self.count += 300
		elif line == 3:
			self.count += 600
		elif line == 4:
			self.count += 1000

		if speed <= 8:
			speed = 8
		else:
			speed = INIT_SPEED - (self.count / 10000)

	def draw_count(self, screen):
#		print 'draw_count'
		pygame.display.set_caption("PyTetris score: %s" %self.count)


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
					pygame.draw.rect(screen, COLOR[self.type], Rect(x+i*20, y+j*20, 20, 20))


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
					pygame.draw.rect(screen, COLOR[color_index], Rect(j*20, i*20, 20, 20))


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
		self.grid = Grid()
		self.block = Block(randint(0,6), 0)
		self.count = Count(0)
		self.score = 0
		self.speed = 20
		self.clock = pygame.time.Clock()

		self.ready()


	def ready(self):
#		if click_button == 1:
			self.begin_game()


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
				if event.key == K_LEFT:
					move_x = -1 * move_left(self.block, self.grid)
				elif event.key == K_RIGHT:
					move_x = +1 * move_right(self.block, self.grid)
				elif event.key == K_DOWN:
					moviable = move_down(self.block, self.grid)
					if moviable == 1:
						move_y = +1 * 1
					else:
						self.block = Block(randint(0,6), 0)
						if self.check_game_over() == 1:
						#	print 'Game Over'
							raw_input('Game Over')
							break

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
		pygame.init()

		self.screen = pygame.display.set_mode((200,400), 0, 32)
		pygame.display.set_caption("PyTetris--0.0.2-dev")

#		print 'Begin Game...'

		drop_interval = 0
		while True:
			self.clock.tick(60)
			drop_interval = drop_interval+1
			self.screen.fill((0,0,0))

			self.check_event()
			if drop_interval % (self.speed*3) == 0:
				drop_interval = 0
				moviable = move_down(self.block, self.grid)
				if moviable == 1:
					move_y = +1 * 1
					self.block.blocky += move_y
				else:
					self.block = Block(randint(0,6), 0)
					if self.check_game_over() == 1:
					#	print 'Game Over'
						raw_input('Game Over')
						break

			score = self.grid.check_tetris()
			self.count.update_score(score, self.speed)
			self.count.draw_count(self.screen)
			self.grid.draw_grid(self.screen)
			self.block.draw_block(self.screen, self.block.blockx*20, self.block.blocky*20)

			pygame.display.update()


def main():
	game = Game()


if __name__ == '__main__':
	main()
