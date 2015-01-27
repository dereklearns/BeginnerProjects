def checktriple(a,b,c): #Function that checks if nums == pythagoraentriplets
	if a*a + b*b == c*c:
		return True
	else:
		return False
while True:
	usernums = [] #Create new list to use

	for i in range(3):
		n = int(raw_input("Enter side\t"))
		usernums.append(n)

	sorted(usernums) #Sort from min to max to grab C value and determine a and b

	print checktriple(*usernums) #Unpacking list