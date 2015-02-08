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

	def isdead(self):
		if self.age > 10:
			return True
		else:
			return False

def displayStats(self):
	print '{0:10}\t{1}\t{2}\t{3:20}\t'.format(self.name, self.sex,self.age,self.color)

bunnies = []
bunniesupdated = []
current_Day = 0

for i in range(5):
	bunnies.append(Bunny())

def able_to_breed(bunny):
	if bunny.sex == "F" and bunny.age >= 2:
		return True
	else:
		return False

def make_bunnies(mother):
	newbaby = Bunny()
	newbaby.color = mother.color
	bunniesupdated.append(newbaby)

while len(bunnies):
	bunnies = sorted(bunnies, key = lambda bunny: bunny.age)
	current_Day += 1

	for bunny in bunnies:

		bunny.age += 1

		if able_to_breed(bunny):
			make_bunnies(bunny)

		if  not bunny.isdead():
			bunniesupdated.append(bunny)
			displayStats(bunny)
		else:
			pass

	del bunnies
	bunnies = bunniesupdated
	del bunniesupdated
	bunniesupdated = []
	print "*" *72
	
	if len(bunnies) > 10:
		random.shuffle(bunnies)
		del bunnies[len(bunnies)//2:] #Deletes list from half to end


print "The bunnies lasted ", current_Day, " days."