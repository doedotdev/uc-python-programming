'''
Benjamin D. Horn
Read from file
Collections
No internet feature
counters
file i/o
9/23/15
'''
import collections
import re
import getopt
import os
import sys

# default file, change here or when prompting the system in command line
file_name = "C:/Users/benja_000/Desktop/Temp/go.txt"
stop_words_file ="C:/Users/benja_000/Desktop/Temp/stop.txt"
number = 10


opts, args = getopt.getopt(sys.argv[1:],"hf:n:s:")
for opt, arg in opts:
    if opt == '-h': # help
        print('-f word file  -n number  -s stop file -h help')
        print('Defaults:')
        print('go.txt find 20 words that dont include those in stop.txt')
        sys.exit() # do not run defaults if they call for help
    elif opt in ("-f"): #file
        file_name = arg
        print("File to Search: ", file_name)
    elif opt in ("-n"): #number of words
        number = arg
        print("Number to find",number)
    elif opt in ("-s"): #stop file name
        stop_words_file = arg
        print("Number to find",number)

c = collections.Counter()
with open(file_name,'r') as f:
    for line in f:
        line = line.lower()
        wordlist = list(line.split())
        c.update(wordlist)


sfile = open(stop_words_file, 'r')
stext = sfile.read().lower()
sfile.close()
stext = re.sub('[^a-z\ \']+', ' ', stext)
stopwordlist = list(stext.split())


for word in stopwordlist:
    del c[word]

print ('Most common no stops:')
i = 0
for word, count in c.most_common(int(number)):
    i = i + 1
    print(i,"-> " , word,": ", count)
