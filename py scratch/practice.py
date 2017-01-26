
filename = 'smallText.rtf'
f = open(filename)
data = f.readlines()
f.close()

print(data)
x = 0
for each in data:
    x=x+1

print(x)