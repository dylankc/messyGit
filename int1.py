import re # use this library for splitting off words

all_words = [] # initialize list to store the words

with open('sampleforint.txt') as f: # best way to open a file
   for line in f:
       line = line.strip() # remove trailing newline
       words = re.split(r'\W+', line) # split the line into words even when you have punctuation
       all_words += words
       # looping is done now, and all lines have been read
all_words = set(all_words) # remove duplicates
all_words = sorted(all_words) # sort (capitalized words will come first)
print(all_words)
