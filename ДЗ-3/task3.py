f = open("input.txt", encoding='utf8')
lines = f.readlines()
f.close()

for line in lines:
    words = line.split()
    for i in range(0,len(words),2):
        print(words[i], end = " ")
    print()
