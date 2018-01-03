import re

filename = open("C:\Users\dylan\Desktop\shorterList.txt", 'r')
fileout = open("C:\Users\dylan\Desktop\List.txt", 'w')
counter = 0
checked = []
words = []
slicer = []
singlelist = []
testRegex = re.compile(r"([a-zA-Z]+)")
i = 0
strfinale = " "


with filename as f_obj:
	lines = f_obj.readlines()




	for line in lines:
		if counter >= 0:
			checked = (line.split(" "))

			counter += 1

			slicer = (checked[:-1])
			for x in slicer:
				#print(x)
				if x.__contains__(""):
					singlelist.append(x.upper())
					if len(x) < 6:
						singlelist.remove(x.upper())

	for idx, val in enumerate(singlelist):

		print((singlelist[0]))
		print((singlelist[3]))
		print((singlelist[:-1]))
		print(len(singlelist))
		print("singlelist[idx] is "+singlelist[idx])
		print("Val is "+val)
