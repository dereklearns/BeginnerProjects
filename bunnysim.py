import random
import time

def loadfile(filename):
    with open(filename, "r") as open_file:
        return [line.strip() for line in open_file]
 
class Bunny(object):
	# pos = (-1,-1)
	def __init__(self):
		self.age = 0
		self.sex = random.choice(("M", "F"))
		self.name = random.choice(male_names if self.sex == "M" else female_names)
		self.radioactive = random.randrange(1,100) <= 2
		self.color = random.choice(colors)
		self.pos = (-1,-1)

	def is_dead(self):
		if not self.radioactive:
			return self.age > 10
		return self.age > 10

	def breedable(self):
		return self.sex == "F" and self.age >= 2 and not self.radioactive

	def get_stats(self):
		return "{name:10}\t{age}\t{sex}\t{color:20}\t{radioactive}".format(name = self.name,
																		age = self.age,
																		sex = self.sex,
																		color = self.color,
																		radioactive = "Healthy" if not self.radioactive else "Radioactive")

def make_baby(mother):
	newbaby = Bunny()
	newbaby.color = mother.color
	return newbaby

def write_grid(board):
	with open("boardtest.txt","a") as f:

		for i in range(25):
			for j in range(25):
				if not board[i][j] == 0 and not board[i][j].radioactive:
					f.write(board[i][j].sex + " ")
				elif not board[i][j] == 0 and board[i][j].radioactive:
					f.write("X ")
				else:
					f.write("0 ")
			f.write("\n")

		f.write("-" * 72 + "\n")


def print_grid(board):
	for i in range(25):
		for j in range(25):
			if not board[i][j] == 0 and not board[i][j].radioactive:
				print board[i][j].sex,
			elif not board[i][j] == 0 and board[i][j].radioactive:
				print "X",
			else:
				print 0,
		print ""
	print "-" * 72

def return_grid(board):
	result = []
	for i in range(25):
		for j in range(25):
			if not board[i][j] == 0 and not board[i][j].radioactive:
				result.append(board[i][j].sex)
			elif not board[i][j] == 0 and board[i][j].radioactive:
				result.append("X")
			else:
				result.append("0")

	return result

#Maybe use filter with function that compares  == 0
def get_empty_coords(board):
	emptycoord = list()
	for i in range(25):
		for j in range(25):
			if board[i][j] == 0:
				emptycoord.append((i,j))
	return emptycoord

def get_normal_bunny_coords(board):
	emptycoord = list()
	for i in range(25):
		for j in range(25):
			if isinstance(board[i][j], Bunny) and not board[i][j].radioactive:
				emptycoord.append((i,j))

	return emptycoord

def move((x,y), bunny, board):
	a, b = bunny.pos
	board[a][b] = 0
	bunny.pos = (x,y)
	board[x][y] = bunny

def find_neighbors(bunny, match):
	#match is presorted list of type
	x, y = bunny.pos
	possiblemoves = []

	if (x+1, y) in match:
		possiblemoves.append((x+1, y))
	if (x+1, y+1) in match:
		possiblemoves.append((x+1, y+1))
	if (x-1, y-1) in match:
		possiblemoves.append((x-1, y-1))
	if (x+1, y-1) in match:
		possiblemoves.append((x+1, y-1))
	if (x-1, y+1) in match:
		possiblemoves.append((x-1, y+1))
	if (x-1, y) in match:
		possiblemoves.append((x-1, y))
	if (x, y+1) in match:
		possiblemoves.append((x, y+1))
	if (x, y-1) in match:
		possiblemoves.append((x, y-1))

	return possiblemoves


def cycle(bunnies, board):
	with open("bunnyinfo.txt", "a") as f:
		for bunny in bunnies[:]: #This creates a copy of bunnies, so can change bunnies in the iterations
			bunny.age += 1
			
			if bunny.is_dead():
				bunnies.remove(bunny)
				x, y = bunny.pos
				board[x][y] = 0
				continue

			if bunny.pos != (-1,-1) and list(filter(lambda x: not x.radioactive, bunnies)):

				possible_moves = find_neighbors(bunny, get_empty_coords(board))

				if possible_moves:
					chosen_move = random.choice(possible_moves)
					move(chosen_move, bunny, board)


			if bunny.breedable():
				male_bunnies = filter(lambda x: x.sex == "M", bunnies)
				if male_bunnies:
					baby = make_baby(bunny)
					moves = find_neighbors(bunny, get_empty_coords(board))
					if moves:
						baby.pos = random.choice(moves)
						move(baby.pos, baby, board)
						bunnies.append(baby)

			if bunny.radioactive:
				normal_bunnies = list(filter(lambda x: not x.radioactive, bunnies))
				if normal_bunnies:

					coords = find_neighbors(bunny, get_normal_bunny_coords(board))
	
					if coords:
						coords = random.choice(coords)
					
					for b in normal_bunnies:
						if b.pos == coords and not b.radioactive:
							b.radioactive = True

			# print bunny.get_stats()

			if bunny.pos == (-1,-1) and len(get_empty_coords(board)) != 0:
				pos = random.choice(get_empty_coords(board))
				move(pos, bunny, board)


		f.write("\n")
		for bunny in bunnies:
			f.write(str(bunny.get_stats()) + "\n")
		f.write("-" * 72)

def main():
	#Initialize bunny list
	bunnies = [Bunny() for i in range(5)]
	
	#Initialize a 3 by 3 board filled with 0's
	board = [[0 for col in range(25)]for row in range(25)]

	with open("bunnyinfo.txt", "w") as f:
		f.write("")

	with open("boardtest.txt", "w") as f:
		f.write("")

	while bunnies:
		cycle(bunnies, board)
		if len(bunnies) > 1000:
			random.shuffle(bunnies)
			bunnies = bunnies[:len(bunnies) // 2]

		# with open("boardtest.txt", "a") as f:
		# 	for i in range(25):
		# 		a = board[i]
		# 		a = str(a)
		# 		f.write(a)
		# 		f.write("\n")
				
		write_grid(board)
		# print_grid(board)
		# with open("bunnyboard.txt", "w") as f:
		# 	f.write(print_grid(board))

	with open("boardtest.txt", "r") as f:
		for line in f:
			if line.find("-") == 0:
				time.sleep(.10)
				print"\n"
			else:
				print line,


if __name__ == '__main__':
	male_names = loadfile("names_male.txt")
	female_names = loadfile("names_female.txt")
	colors = loadfile("colorlist.txt")
	main()

male_names = loadfile("names_male.txt")
female_names = loadfile("names_female.txt")
colors = loadfile("colorlist.txt")