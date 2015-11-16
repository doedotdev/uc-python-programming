'''
Benjamin Horn
Homework for Week 3
-os walk
- string work
- command line parsing
- and more
9/14/2015
'''

import os, sys, getopt

temp_dir = '.' # Fill so it will run if no dir given (-d)
temp_key = 'tkinter'# Fill so it will run if no key given (-k)

opts, args = getopt.getopt(sys.argv[1:],"hd:k:")
for opt, arg in opts:
    if opt == '-h': # option help
        print('-d directory     -k keyword     -h help')
        print('default: -d .')
        print('default: -k tkinter')
        sys.exit() # do not run defaults if they call for help
    elif opt in ("-d"): # option give directory
        temp_dir = arg 
    elif opt in ("-k"): # option give keyword
        temp_key = arg
print('Directory is ', temp_dir)
print('Keyword is ', temp_key)

count = 0
for (dirs, subs, fils) in os.walk(temp_dir):
    for each in fils:
            temp_file = os.path.join(dirs,each)
            try:
                if str(temp_key) in (open(temp_file).read()):
                    count = count + 1
            except:
                pass
print('In the directory,',temp_dir,',the keyword',temp_key,'is found,',count,'times')
