# 20/07/2021 - CGOL.py
# Conway's Game of Life made in pygame

# imports
import pygame
import random
import copy

# width and height of each cell
cellSize = 10

# initialise grid
gridWidth = 50
gridHeight = 50

# init screen
screenWidth = gridWidth * cellSize
screenHeight = gridHeight * cellSize

screen = pygame.display.set_mode((screenWidth,screenHeight))

#initialise game
pygame.init()
pygame.display.set_caption("PyGame of Life")

#clock
clock = pygame.time.Clock()

class Grid:
	# constructor
	def __init__(self, w, h):
		self.width = w
		self.height = h

		self.grid = [[[0,0] for row in range(self.height)] for col in range(self.width)]

	# method to set the state of a cell
	def setCell(self, x, y, stat):

		# ignore if same state
		if self.grid[x][y][0] == stat:
			return

		# set the state
		self.grid[x][y][0] = stat

		# wrapping
		xLeft = x-1
		
		if x == gridWidth-1:
			xRight = 0
		else:
			xRight = x+1
		
		yUp = y-1
		
		if y == gridHeight-1:
			yDown = 0
		else:
			yDown = y+1

		# increment neighboring cells' neighbor counts if stat is 1
		# otherwise decrement
		
		self.grid[xLeft][yUp][1] += -1 + (2 * stat) 
		self.grid[xLeft][y][1] += -1 + (2 * stat)
		self.grid[xLeft][yDown][1] += -1 + (2 * stat)

		self.grid[x][yUp][1] += -1 + (2 * stat)
		self.grid[x][yDown][1] += -1 + (2 * stat)
		
		self.grid[xRight][yUp][1] += -1 + (2 * stat)
		self.grid[xRight][y][1] += -1 + (2 * stat)
		self.grid[xRight][yDown][1] += -1 + (2 * stat)

	def nextGen(self):
		# create a temp copy of the grid and find the next generation based off of that copy

		self.tempGrid = copy.deepcopy(self.grid)

		for col in range(gridWidth):
			for row in range(gridHeight):
				# conditions:
				# if less than 2 or more than 3 neighbors, change to 0
				# if exactly 3 neighbors, change to 1

				if self.grid[col][row][0] == 0:
					if self.tempGrid[col][row][1] == 3:
						self.setCell(col, row, 1)

				elif self.grid[col][row][0] == 1:
					if self.tempGrid[col][row][1] < 2 or self.tempGrid[col][row][1] > 3:
						self.setCell(col, row, 0)
		
def randomBoard(board):

	for x in range(gridWidth):
		for y in range(gridHeight):
			board.setCell(x, y, random.choice([0,0,0,1]))

def drawBoard(board):
	
	colors = [(0,0,0), (255,255,255)]

	for xCell in range(gridWidth):
		for yCell in range(gridHeight):
			pygame.draw.rect(screen, colors[board.grid[xCell][yCell][0]], pygame.Rect(xCell*cellSize, yCell*cellSize, cellSize, cellSize))

	'''
	# for debugging
	for row in range(gridHeight):
		for col in range(gridWidth):
			print(col, row, board.grid[col][row],end='')
		print()
	'''
	
def main():

	g = Grid(gridWidth, gridHeight)

	randomBoard(g)

	running = True

	while running:		

		clock.tick(15)

		screen.fill((0,0,0))

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False

		drawBoard(g)

		g.nextGen()

		pygame.display.flip()

if __name__ == "__main__":
	main()