import sys
import string
import re

f = open('C:\\Users\\dylan\\desktop\\book1.txt', 'r') #open file
words = {}

words_keys = sorted(words)
output_file = open("C:/Users/dylan/desktop/book1_lines.txt", "w")
output_file.write("There are {0} words in the file.\n".format(len(words)))
output_file.write("Some of the words in your file are:\n")
for key in words_keys:
    output_file.write("{0}: {1}\n".format(key, words[key]))
output_file.close()