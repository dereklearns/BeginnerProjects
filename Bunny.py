import random

bunnies = [] #Initialize list

class Bunny(object):

	def __init__(self, id):
		self.id = id

for i in range(5000000):
	rng = random.random()	
	
	bunnies.append(Bunny(rng))


print "done adding"
print "now sorting"
newlist = sorted(bunnies, key=lambda bunny: bunny.id)
'''
for bunny in newlist:
	print bunny.id
'''