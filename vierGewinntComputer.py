from vierGewinntModel import *
import copy

# class for a node in the Tree, it's a linked list
class vierGewinntNode:
	def __init__(self, grid, playedCol, parent):
		self._grid = grid
		self._children = []
		self._score = 0
		self._parent = parent
		self._col = playedCol

	def getGrid(self):
		return self._grid

	def getCol(self):
		return self._col
	
	def getChildren(self):
		return self._children
	def addChild(self, child):
		self._children.append(child)

	def getParent(self):
		return self._parent
	def setParent(self, parent):
		self._parent = parent

	def getScore(self):
		return self._score
	def setScore(self, score):
		self._score = score

# realy basic and retarded AI
# It mistreats the vierGewinntNode class :(
class vierGewinntStupidComputer:
	def __init__(self, playerSign):
		self._model = vierGewinntModel()
		self._sign = playerSign

	def makeAMove(self, grid):
		# generate the possibilites for the next move
		baseGrid = copy.deepcopy(grid)
		self._model.setGrid(baseGrid)
		moves = []
		for x in range(7):
			self._model.play(x, self._sign)
			node = vierGewinntNode(self._model.getGrid(), x, None)
			if True:
				winner = self._model.checkWinner()
				if winner == 1:
					node.setScore(500)
				elif winner == 2:
					node.setScore(-500)
				else:
					node.setScore(self.evaluateGameState(node.getGrid()))
				moves.append(node)
			self._model.setGrid(copy.deepcopy(grid))
		
		# search the best move
		bestScore = 0
		bestCol = 0
		prefix = 1
		if self._sign == 2:
			prefix = -1
		for node in moves:
			if node.getScore()*prefix > bestScore:
				bestScore = node.getScore()*prefix
				bestCol = node.getCol()
		
		print(str(bestScore)+" at col "+str(bestCol))
		return bestCol
		


	def evaluateGameState(self, grid):
		# copied from https://softwareengineering.stackexchange.com/questions/263514/why-does-this-evaluation-function-work-in-a-connect-four-game-in-java
		# There are better functions, but it's ready made so …
		evaluationTable = [[3, 4, 5, 5, 4, 3],
							[4, 6, 8, 8, 6, 4],
							[5, 8, 11, 11, 8, 5],
							[7, 10, 13, 13, 10, 7],
							[5, 8, 11, 11, 8, 5],
							[4, 6, 8, 8, 6, 4],
							[3, 4, 5, 5, 4, 3]]
		sum = 0
		for x in range(X_TILES):
			for y in range(Y_TILES):
				if grid[x][y] == 1:
					sum += evaluationTable[x][y]
				elif grid[x][y] == 2:
					sum -= evaluationTable [x][y]
		return sum
	