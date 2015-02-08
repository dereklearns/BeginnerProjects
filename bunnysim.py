import random
male_names = []
female_names = []
colors = []

with open("names_male.txt", "r") as f:
	for line in f:
		male_names.append(line.strip()) #Adds each name into list, and strips of /n's

with open("names_female.txt", "r") as f:
	for line in f:
		female_names.append(line.strip())

with open("colorlist.txt", "r") as f:
	for line in f:
		colors.append(line.strip())

class Bunny(object):
	
	age = -1
	weight = -1
	color = "-1"
	name = "-1"
	sex = "-1"

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

	def deathcheck(self):
		if self.age > 10:
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
for bunny in bunnies:
	bunny.age = random.randrange(1,10)

i = 0
while i < 15:
	
	for bunny in bunnies:
		bunny.age += 1
		if bunny.age < 15:
			bunnies2.append(bunny)
		else:
			pass
		displayStats(bunny)

	del bunnies
	bunnies = bunnies2
	del bunnies2
	bunnies2 = []
	i += 1
	print "*" *72