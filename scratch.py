import string

open_file = "E:/sampleforint.txt"
lst = list()
counter = 0
stringone = ""


with open(open_file) as separator_obj:
	lines = separator_obj.readlines()
	counter += 1
	print(lines)
	stringone = (lines.sort())
	#print(stringOne)
Numtwo = (len(stringone))
	#print(Numtwo)
