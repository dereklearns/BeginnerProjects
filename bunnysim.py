import random

male_names = []
female_names = []
colors = []

def loadfile(filename, listname):
	with open(filename, "r") as f:
		for line in f:
			listname.append(line.strip())

loadfile("names_male.txt", male_names)
loadfile("names_female.txt", female_names)
loadfile("colorlist.txt", colors)

class Bunny(object):
	
	age = 0
	weight = 5
	color = "-1"
	name = "-1"
	sex = "-1"
	pregnant = False

	def __init__(self):
		self.color = random.choice(colors)
		self.sex = random.choice(["M", "F"])
		
		if self.sex == "M":
			self.name = random.choice(male_names)
		else:
			self.name = random.choice(female_names)		


	def eat(self, food):
		#print self.name, " eats ", food.name
		self.weight += food.value

	def isdead(self):
		if self.age > 50:
			return True
		elif self.weight <= 0:
			return True
		else:
			return False

class Food(object):
 
	name = "-1"
	value = 1

	def __init__(self, name, value):
		self.name = name
		self.value = value

def displayStats(self):
	print '{0:10}\t{1}\t{2}\t{3:20}\t{4}'.format(self.name, self.sex,self.age,self.color,self.weight)

carrot = Food('Carrot', 1)

bunnies = []
bunnies2 = []
current_Day = 0

for i in range(5):
	bunnies.append(Bunny())



def able_to_breed(bunny):
	if bunny.sex == "F" and bunny.pregnant == False:
		return True
	else:
		return False

def make_bunnies():
	for i in range(6):
		bunnies2.append(Bunny())

while len(bunnies):
	bunnies = sorted(bunnies, key = lambda bunny: bunny.name)
	current_Day += 1

	for bunny in bunnies:
		bunny.weight += random.choice([-2,-1,1,2])
		bunny.age += 1

		if able_to_breed(bunny):
			if random.choice([1,2,3,4,5]) == 3:
				make_bunnies()

		if  not bunny.isdead():
			bunnies2.append(bunny)
		else:
			pass

		displayStats(bunny)

	del bunnies
	bunnies = bunnies2
	del bunnies2
	bunnies2 = []
	print "*" *72
	raw_input()

print "The bunnies lasted ", current_Day, " days."