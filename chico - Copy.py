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

	