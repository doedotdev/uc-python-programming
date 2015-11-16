
import os, sys, getopt

temp_dir = ''
temp_key = ''

opts, args = getopt.getopt(sys.argv[1:],"hd:k:")
for opt, arg in opts:
    if opt == '-h':
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit()
    elif opt in ("-d"):
        temp_dir = arg
    elif opt in ("-k"):
        temp_key = arg
print('Directory is ', temp_dir)
print('Keyword is ', temp_key)

count = 0
for (dirs, subs, fils) in os.walk(temp_dir):
    #print('[' + dirname + ']')
    for each in fils:
            temp_file = os.path.join(dirs,each)
            try:
                if str(temp_key) in (open(temp_file).read()):
                    #print(temp_file +'XXXXXXXXXXX')
                    count = count + 1
            except:
                pass
print(count)
