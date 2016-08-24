'''
Benjamin Horn
Homework for Week 4
-os walk
- string work
- command line parsing
- file size
- find largest and smallest files
9/14/2015
'''

import os, sys, getopt, operator

temp_dir = '.' # Fill so it will run if no dir given (-d)
temp_key = 'tkinter'# Fill so it will run if no key given (-k)
temp_num = '1' # give smallest and largest 1 as default
opts, args = getopt.getopt(sys.argv[1:],"hd:k:n:")
for opt, arg in opts:
    if opt == '-h': # option help
        print('-d directory     -k keyword    -n number    -h help')
        print('default: -d .')
        print('default: -k tkinter')
        print('number: -n 1')
        sys.exit() # do not run defaults if they call for help
    elif opt in ("-d"): # option give directory
        temp_dir = arg 
    elif opt in ("-k"): # option give keyword
        temp_key = arg
    elif opt in ("-n"): #option smallest and largest files
        temp_num = arg
print('Directory is ', temp_dir)
print('Keyword is ', temp_key)

count = 0
file_size = [] # empty to store te file and the temp_dict = {'file_name': 'file', 'size': 10}

for (dirs, subs, fils) in os.walk(temp_dir):
    for each in fils:
            temp_file = os.path.join(dirs,each)
            try:
                if str(temp_key) in (open(temp_file).read()):
                    temp_dict = {'file_name': temp_file, 'file_size': os.path.getsize(temp_file)}
                    file_size.append(temp_dict)
                    count = count + 1
            except:
                pass
print('In the directory,',temp_dir,',the keyword',temp_key,'is found,',count,'times')

'''
After this showing how to get the largest and smallest files
'''

new_list = sorted(file_size, key=operator.itemgetter('file_size'))
print()
print('. . . . . . . . . . . .')
temp_num = int(temp_num)
print(temp_num,'Smallest Files')
for i in range(0, temp_num):
    print(new_list[i])

print()
print()

print(temp_num,'Largets Files')
for i in range(len(new_list)-1,len(new_list) - temp_num -1, -1):
    print(new_list[i])
    
