'''
Benjamin Horn
OS walk
c:\Python34\python test.py . tkinter

'''
import os
import sys

count  = 0
search_dir = (sys.argv[1])
search_key = (sys.argv[2])

print(sys.argv[1])
print(sys.argv[2])

if search_dir == '':
    search_dir = '.'
if search_key =='':
    search_key = 'tkinter'

for (dirname, subshere, fileshere) in os.walk(search_dir):
    #print('[' + dirname + ']')
    for fname in fileshere:
            temp_file = os.path.join(dirname,fname)
            try:
                if str(search_key) in (open(temp_file).read()):
                    #print(temp_file +'XXXXXXXXXXX')
                    count = count + 1
            except:
                pass
print(count)

'''
        if fname.endswith('py'):



'''
