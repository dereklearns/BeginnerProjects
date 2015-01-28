grade = 59

if grade < 60:
	print "F"
elif grade >= 60 and grade < 70:
	print "D"
elif grade >= 70 and grade < 80:
	print "C"
elif grade >= 80 and grade < 90:
	print "B"
elif grade >= 90 and grade <= 99:
	print "A"
elif grade == 100:
	print "Perfect Score"
else:
	print "unknown score"