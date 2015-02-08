import random
name_list = []
colors = []
with open("names_male.txt", "r") as f:
	for line in f:
		name_list.append(line.strip()) #Adds each name into list, and strips of /n's

with open("colorlist.txt", "r") as f:
	for line in f:
		colors.append(line.strip())

class Bunny(object):
	
	age = 0
	weight = 5
	color = "-1"
	name = "-1"
	sex = "M"

	def __init__(self):
		self.color = random.choice(colors)
		self.name = random.choice(name_list)


	def eat(self, food):
		#print self.name, " eats ", food.name
		self.weight += food.value


class Food(object):
 
	name = "-1"
	value = 1

	def __init__(self, name, value):
		self.name = name
		self.value = value

def displayStats(self):
	print '{0:10}\t{1}\t{2}\t{3}\t{4}'.format(self.name, self.sex,self.age,self.color,self.weight)

carrot = Food('Carrot', 1)

bunnies = []


for i in range(10):
	bunnies.append(Bunny())

for i in range(5):
	for bunny in bunnies:
		bunny.eat(carrot)
		displayStats(bunny)

	print "-" * 72

