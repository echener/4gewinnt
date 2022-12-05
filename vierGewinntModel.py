X_TILES = 7
Y_TILES = 6

class vierGewinntModel:
	def __init__(self):
		self._grid = [[0 for x in range(6)] for y in range(7)]
		self._move = 0

	def getGrid(self):
		return self._grid

	def setGrid(self, grid):
		self._grid = grid

	def play(self, xPos, player):
		if self._isFileFull(xPos):
			xPos = None

		if xPos != None:
			self._grid[xPos][self._returnHighestTile(xPos)] = player
			self._move = self._move + 1

	def getCurrPlayer(self):
		player = 0
		if self._move%2 == 0:
			player = 1
		else :
			player = 2
		return player
	
	def getMoves(self):
		return self._move

	def _returnHighestTile(self, xPos):
		y = 0
		for y in range(6):
			if self._grid[xPos][y] == 0:
				return y
		return 6

	def _isFileFull(self, xPos):
		if xPos == None:
			return True
		elif self._returnHighestTile(xPos) > 5:
			return True
		else:
			return False

	def checkWinner(self):
		# horizontal
		for y in range(Y_TILES):
			for x in range(X_TILES-3):
				if self._grid[x][y] != 0:
					if self._grid[x][y] == self._grid[x+1][y] == self._grid[x+2][y] == self._grid[x+3][y]:
						return self._grid[x][y]

		# vertical
		for x in range(X_TILES):
			for y in range(Y_TILES-3):
				if self._grid[x][y] != 0:
					if self._grid[x][y] == self._grid[x][y+1] == self._grid[x][y+2] == self._grid[x][y+3]:
						return self._grid[x][y]
		
		# diagonal W->E
		for y in range(3):
			for x in range(4):
				if self._grid[x][y] != 0:
					if self._grid[x][y] == self._grid[x+1][y+1] == self._grid[x+2][y+2] == self._grid[x+3][y+3]:
						return self._grid[x][y]

		# diagonal E->W
		for y in range(3):
			for x in range(X_TILES-1, 2, -1):
				if self._grid[x][y] != 0:
					if self._grid[x][y] == self._grid[x-1][y+1] == self._grid[x-2][y+2] == self._grid[x-3][y+3]:
						return self._grid[x][y]
	