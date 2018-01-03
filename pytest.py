open_file = open("E:/intone")
lst = list() 
puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]

for line in open_file:  
    line = line.rstrip()
    words = line.split()
    for word in words:  
        if word not in lst:
            lst.append(word)

lst.sort()
print(lst)
print (len(lst))

for word in lst:
 	print(word)#+"\n")

