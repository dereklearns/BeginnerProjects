def verse(num):
	if num == 1:
		return str(num) + " bottle of beer on the wall"	 #Adjusts to bottle when 1 left
	else:
		return str(num) + " bottles of beer on the wall"			

counter = 99 #initialize counter
while counter > 0:

	print verse(counter)
	temp = verse(counter)

	if counter < 10: #Adjusts slice when ## goes to #
		print temp[0:17]
	else:
		print temp[0:18]

	print "take one down, pass it around "
	print verse(counter) + "\n"

	counter -= 1