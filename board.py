board = list()

for col in range(5):
	board.append([])
	for row in range(5):
		board[col].append(0)

def printboard():
	for row in board:
		print row
	print "*" * 72

printboard()
board[3][2] = 1
printboard()