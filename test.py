import string
#using key, val of dictionary to parse data
fhand = open('sampleforint.txt')
counts = dict()
for line in fhand:
    line = line.translate(string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

    lst = list()
    for key, val in counts.items():
        lst.append( (val, key) )

    lst.sort(reverse=True)#(reverse=True)
    counter = 0
    for key, val in lst:
        print(key, val)
