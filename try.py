
open_file = open('E:\sampleforint.txt') #open file

lst = list() #create empty list 
counter = 0

for line in open_file:  #1st for loop strip white space and split string into list of words 
    line = line.strip()
    words = line.split(" ")
    for word in words:
        counter += 1
        lst.append(word.strip().split())
        #print(word.split())
        #print(sorted(lst))
        #print(lst[:])
        #print(sorted(lst))
        print(lst[0:])
        print(sorted(lst))
    print(sorted(lst))



#            :  #nested for loop, check if the word is in list and if not append it to the list
        #!!!!!!!!!!if word not in lst:
        #!!!!!!!!!!lst.append(word)
#       if word not in lst:
#           lst.append(word)
#st.sort() #sort the list of words: alphabetically
#print(lst.sort()) #print the list of words