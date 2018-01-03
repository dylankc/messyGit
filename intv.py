import re
outfile = open("E:/sampleforint.txt", 'w')
placeref = """Adult beavers have long flat tails that are about a foot long. Beavers slap their tails on the water surface as an alarm to alert the colony when they sense danger. Female beavers are larger than male beavers of the same age. Prior to European immigration there were over 60 million beavers in North America. Due primarily to over trapping beavers were an endangered species in the early part of the 20th Century. Beavers are very active on Pinterest and often are considered social media mavens. Tiny beavers (Microtheriomys brevirhinus) lived in Oregon 28 Million Years Ago. They were 1/10 the size of modern beavers."""

counter = 0
intcounter = 0
lst = []
#finale = []

def extractor(placeref):
    words = re.findall('[\w]', placeref)
    numba = len(words)
    if numba == 1:
        return words[0]
    elif numba > 0:
        return words[0].lower() + ''.join(map(str.title, words[1:]))
    else :
        return ' '

finale = (str(filter(str, map(extractor, placeref))))   #strip("\n")))))
#print(cleanlist.remove('\n'))
print(finale)


#print(cleanlist[intcounter])



#print(cleanlist)
## for line in outfile.readlines():
    #sep = (cleanlist.splitlines())
#for y in sep:
    #print(y)
#    almostone = lst.append(sep)
#    almosttwo = list(sorted(lst[0:]))
#print(almostone)
#for x in almost:
#print(almost[0:-1]), len(almost)
#print(sorted(almost))
#print(almost.count(str))


