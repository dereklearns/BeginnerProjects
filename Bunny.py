import random

bunnies = [] #Initialize list

class Bunny(object):

	def __init__(self, id):
		self.id = id

for i in range(10):
	rng = random.random()	
	
	bunnies.append(Bunny(rng))

newlist = sorted(bunnies, key=lambda bunny : bunny.id)
for bunny in bunnies:
	print bunny.id

print "*" * 42

for bunny in newlist:
	print bunny.id
