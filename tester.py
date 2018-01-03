import re
import string

filename = open("C:/Users/Dylan/Desktop/New Folder/punc.txt")
lines = filename.readlines()
emptyList = []


for word in lines:
	word = str(word)
	
	for char in string.punctuation:
		if len(word) > 4:
			word = word.replace(char, '')
			emptyList.append(word)
			print(word)
		else:
			
			#print(word)


	#re.sub(r'[\w]', ' ', word)
	#regex.findall(word[, 0[, endpos]])


	








# numLines = 0
# numWords = 0
# numChars = 0
# lst = []
# lstcounter = 0


# with open(filename, 'r') as file:
# 	while lstcounter >= 0:
# 	#for line in file:
# 		wordsList.slice(0, -1, 1)
# 		numWords += 1
# 		numChars += 1
# 		print(wordsList[lstcounter])
# 		lstcounter += 1
# 		numLines += 1
# 		print(heyyou.split(""))
# 		#--------------------
# #print("number of lines, words ")
		

# 		#print(sorted(wordsList))#.sort())
# print(sorted(wordsList))#.sort())
# #print(numLines)