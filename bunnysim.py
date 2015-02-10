import random
 
def loadfile(filename):
    with open(filename, "r") as open_file:
        return [line.strip() for line in open_file]
 
class Bunny(object):
	def __init__(self):
		self.age = 0
		self.sex = random.choice(("M", "F"))
		self.name = random.choice(male_names if self.sex == "M" else female_names)
		self.radioactive = random.randrange(1,100) <= 2
		self.color = random.choice(colors)

	def isdead(self):
		if not self.radioactive:
			return self.age > 10
		return self.age > 50

	def breedable(self):
		return self.sex == "F" and self.age >= 2 and not self.radioactive

	def getstats(self):
		return "{name:10}\t{age}\t{sex}\t{color}\t{radioactive}".format(name = self.name,
																		age = self.age,
																		sex = self.sex,
																		color = self.color,
																		radioactive = "Healthy" if not self.radioactive else "Radioactive")

def makebaby(mother):
	newbaby = Bunny()
	newbaby.color = mother.color
	return newbaby


def cycle(bunnies):
	with open("bunnyinfo.txt", "a") as f: #using "a", doesn't overwrite but adds new write statements
		for bunny in bunnies[:]: #This creates a copy of bunnies, so can change bunnies in the iterations
			bunny.age += 1
			
			if bunny.isdead():
				bunnies.remove(bunny)
				continue

			if bunny.breedable():
				male_bunnies = filter(lambda x: x.sex == "M", bunnies)
				if male_bunnies:
					bunnies.append(makebaby(bunny))

			if bunny.radioactive:
				normal_bunnies = list(filter(lambda x: not x.radioactive, bunnies))
				if normal_bunnies:
					unlucky_bunny = random.choice(normal_bunnies)
					bunnies[bunnies.index(unlucky_bunny)].radioactive = True

			print bunny.getstats()
			
			f.write(str(bunny.getstats())  + "\n")


def main():
	bunnies = []
	for i in range(5):
		bunnies.append(Bunny())

	while bunnies:
		cycle(bunnies)
		if len(bunnies) > 1000:
			random.shuffle(bunnies)
			bunnies = bunnies[:len(bunnies) // 2]

if __name__ == '__main__':
    male_names = loadfile("names_male.txt")
    female_names = loadfile("names_female.txt")
    colors = loadfile("colorlist.txt")
    main()