f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

array = []
start = int(lines[0].split()[0])
stop = int(lines[0].split()[1])
step = int(lines[0].split()[2])

for i in lines[1].split():
    array.append(int(i))
    
array[start:stop:step] = range(start, stop, step)
 
print(array)
