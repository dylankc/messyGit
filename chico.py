

filecommon = open('most_common.txt')
filewords = open('write.txt')
lines = filecommon.readlines()
liness = filewords.readlines()
counter = 0
commonwords = []
origwords = []

for line in lines:
	commonwords.append(line)
#print(commonwords[0:10])
for lne in liness:
	origwords.append(lne)
	print(counter)
	if commonwords.contains(origwords[counter]):
		print(commonwords.__contains__(origwords[counter]))
		print(counter)
		origwords.remove(counter)
		counter += 1
print(counter)

'''
import random

file = open('shorterList.txt')
fileout = open('write.txt', 'w')
randwordpos = random.randrange(0, 10283, 1)
lines = file.readlines()
counter = 0

for line in lines:
	fileout.write(line)
	counter = counter + 1
	print(line)
	print(counter)
print(randwordpos)
fileout.close()
'''
	