def reduce(n):
	quarter = 25
	dime = 10
	nickle = 5
	penny = 1

	qcount = 0
	dcount = 0
	ncount = 0
	pcount = 0

	while n > 0:
		print n
		if n - quarter >= 0:
			n -= quarter
			qcount += 1
		elif n - dime >= 0:
			n -= dime
			dcount += 1
		elif n - nickle >= 0:
			n -= nickle
			ncount += 1
		elif n - penny >= 0:
			n -= penny
			pcount += 1

	return (qcount,dcount,ncount,pcount)

amount = 67

print reduce(amount)

