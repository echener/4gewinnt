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
		self._model = vierGewinntModel(False)
		self._sign = playerSign

	def makeAMove(self, grid):
		# generate the possibilites for the next move
		self._model.setGrid(copy.deepcopy(grid))
		moves = []
		for x in range(7):
			self._model.play(x, self._sign)
			node = vierGewinntNode(self._model.getGrid(), x, None)
									
			winner = self._model.checkWinner()  # TODO check if grid changed at all (full column)
			if winner == 1:
				node.setScore(500)
			elif winner == 2:
				node.setScore(-500)
			else:
				node.setScore(self.evaluateGameState(node.getGrid()))
			moves.append(node)
			self._model.setGrid(copy.deepcopy(grid))

		# try to find possible connect fours for the ennemy
		self._model.setGrid(copy.deepcopy(grid))
		sign = 1
		if self._sign == 1:
			sign = 2
		for x in range(7):
			self._model.play(x, sign)
			node = vierGewinntNode(self._model.getGrid(), x, None)
			winner = self._model.checkWinner()
			if winner == sign:
				if winner == 1:
					node.setScore(-475)
				else:
					node.setScore(475)
				moves.append(node)
			self._model.setGrid(copy.deepcopy(grid))

		# prevent the player from making a "fork" at the beginning
		if self._model.getGrid()[2][0] == 1 or self._model.getGrid()[3][0] == 1 or self._model.getGrid()[4][0] == 1:
			if self._model.getGrid()[3][0] == 0:
				node = vierGewinntNode(self._model.getGrid(), 3, None)
				node.setScore(-450)
				moves.append(node)
			elif self._model.getGrid()[2][0] == 0:
				node = vierGewinntNode(self._model.getGrid(), 2, None)
				node.setScore(-450)
				moves.append(node)
			elif self._model.getGrid()[4][0] == 0:
				node = vierGewinntNode(self._model.getGrid(), 4, None)
				node.setScore(-450)
				moves.append(node)
		
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
		
class vierGewinntMinMaxComputer:
	def __init__(self, sign):
		self._model = vierGewinntModel()
		self._sign = sign

	def makeAMove(self, grid, searchDepth):
		# create the tree
		tmp_model = vierGewinntModel()
		tree = vierGewinntNode(grid, None, None)
		head = tree
		for i in range(searchDepth):
			for ii in range(X_TILES):
				tmp_model.setGrid(copy.deepcopy(grid))
				tmp_model.play(ii, self._sign)
				head.addChild(vierGewinntNode(tmp_model.getGrid(), ii, head))

	def addChildren(self, node, grid, depth):
		head = node
		tmp_model = vierGewinntModel()
		for poss in range(X_TILES):
			tmp_model.setGrid(copy.deepcopy(grid))
			tmp_model.play(poss, self._sign)
			head.addChild(vierGewinntNode(tmp_model.getGrid(), poss, head))
			if 0 < depth:
				self.addChildren((head.getChildren())[poss], tmp_model.getGrid(), depth-1)


	# 500 means won/lost, positive means 1 is winning; neg 2 is winning
	def evaluateGameState(self, grid):
		eval_model = vierGewinntModel()
		eval_model.setGrid(copy.deepcopy(grid))
		winner = eval_model.checkWinner()
		if winner == 1:
			return 500
		elif winner == 2:
			return -500
		
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