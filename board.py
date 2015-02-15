import bunnysim
import random

def printgrid(board):
	for i in range(10):
		for j in range(10):
			if not board[i][j] == 0 and not board[i][j].radioactive:
				print board[i][j].sex,
			else:
				print 0,
		print ""
	print "-" * 72


#Maybe use filter with function that compares  == 0
def getemptycoords(board):
	emptycoord = list()
	for i in range(10):
		for j in range(10):
			if board[i][j] == 0:
				emptycoord.append((i,j))
	return emptycoord

#Initialize a 3 by 3 board filled with 0's
board = list() #2d array [col][row], very confusing in python compared to c++, jeeze
for row in range(10):
	board.append([])
	for col in range(10):
		board[row].append(0)

printgrid(board)

def spawn((a,b), bunny, board):
	x, y = bunny.pos
	board[x][y] = 0
	bunny.pos = (a,b)
	board[a][b] = bunny

printgrid(board)
bunnies = list()

for i in range(5):
	obj = bunnysim.Bunny()
	obj.pos = random.choice(getemptycoords(board))
	bunnies.append(obj)
	spawn(obj.pos, obj, board)

printgrid(board)




