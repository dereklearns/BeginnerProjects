import random

bunnies = [] #Initialize list

class Bunny(object):
	value = 0

	def __init__(self, id):
		self.id = id

for i in range(10):
	rng = random.random()	
	bunnies.append(Bunny(rng))

for bunny in bunnies:
	bunny.value = random.random()

newlist = sorted(bunnies, key=lambda bunny : bunny.id)


for bunny in bunnies:
	print bunny.id

print "*" * 42

for bunny in newlist:
	print bunny.id

print "-" * 42

new2list = sorted(bunnies, key=lambda bunny : bunny.value) #key=lambda caseSensative : caseSensative.value 
for bunny in new2list:
	print bunny.value
