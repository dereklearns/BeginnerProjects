colors = []

with open("colors.txt", "r") as f:
	for line in f:
		newline = ""
		for letter in line:
			
			if letter == "#":
				break

			else:
				newline += letter
				
		colors.append(newline.strip())	

print colors

with open("newcolors.txt", "w") as f:
	for color in colors:
		f.write(color + "")