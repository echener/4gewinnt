from vierGewinntModel import *

# class for a node in the Tree, it's a linked list
class vierGewinntNode:
	def __init__(self, grid, parent):
		self._grid = grid
		self._children = []
		self._score = 0
		self._parent = parent

	def getGrid(self):
		return self._grid
	
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

# The class for the stupid AI
class vierGewinntStupidComputer:
	def __init__(self):
		self._model = 0

	def makeAMove(self, model):
		self._model = model
		

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
	